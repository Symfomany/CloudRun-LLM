from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vllm import LLM, SamplingParams
import asyncio

app = FastAPI()

class Query(BaseModel):
    prompt: str

class ModelLoad(BaseModel):
    model_name: str

# Dictionnaire global pour stocker les instances de modèle
models = {}

@app.post("/load_model")
async def load_model(model: ModelLoad):
    try:
        # Charger le modèle avec vLLM
        llm = LLM(model=model.model_name)
        models[model.model_name] = llm

        # Générer un texte simple pour vérifier le chargement
        sampling_params = SamplingParams(temperature=0.7, max_tokens=50)
        outputs = llm.generate("Generate a simple hello world program in Python", sampling_params)

        return {
            "message": f"Model {model.model_name} loaded successfully",
            "sample_output": outputs[0].outputs[0].text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load model: {str(e)}")

@app.post("/generate")
async def generate(query: Query):
    if "qwen2.5-coder" not in models:
        raise HTTPException(status_code=400, detail="Model not loaded. Please load the model first.")

    try:
        llm = models["qwen2.5-coder"]
        sampling_params = SamplingParams(temperature=0.7, max_tokens=100)
        
        start_time = asyncio.get_event_loop().time()
        outputs = llm.generate(query.prompt, sampling_params)
        end_time = asyncio.get_event_loop().time()

        total_duration = end_time - start_time
        
        return {
            "response": outputs[0].outputs[0].text,
            "total_duration": total_duration,
            "prompt_tokens": outputs[0].prompt_token_ids,
            "output_tokens": outputs[0].outputs[0].token_ids,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "OK"}
