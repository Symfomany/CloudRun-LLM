from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import ollama

app = FastAPI()


class Query(BaseModel):
    prompt: str

class ModelLoad(BaseModel):
    model_name: str

@app.post("/load_model")
async def load_model(model: ModelLoad):
    async with httpx.AsyncClient() as client:
        try:
             # Pull (télécharger) le modèle
            ollama.pull(model.model_name)
            # Charger le modèle en mémoire en générant un texte simple
            response = ollama.generate(model=model.model_name, 
                                    prompt="Generate a simple hello world program in Python")
            
            return {"message": f"Model {model.model_name} loaded successfully", 
                    "sample_output": response['response']}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to load model: {str(e)}")
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Failed to connect to Ollama server")


@app.post("/generate")
async def generate(query: Query):
    try:
        response = ollama.generate(model="qwen2.5-coder", prompt=query.prompt)
        return {
            "response": response['response'],
            "total_duration": response['total_duration'],
            "load_duration": response['load_duration'],
            "prompt_eval_count": response['prompt_eval_count'],
            "eval_count": response['eval_count'],
            "eval_duration": response['eval_duration']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "OK"}
