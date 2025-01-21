# Gcloud

gcloud est l'outil CLI principal pour Google Cloud Platform. 

Il permet de gérer la plupart des ressources et services Google Cloud, notamment :
Créer et gérer des instances Compute Engine
Gérer des clusters Kubernetes Engine
Configurer Cloud SQL
Gérer les autorisations IAM
Déployer des applications App Engine
Et bien plus encore

Pour gérer des machines virtuelles (VM) en ligne de commande avec gcloud, voici les principales commandes à connaître :

## Création de VM

Pour créer une nouvelle VM :

```bash
gcloud compute instances create NOM_VM --machine-type=TYPE --image-project=PROJET --image-family=FAMILLE_IMAGE
```

Par exemple :

```bash
gcloud compute instances create ma-vm --machine-type=e2-micro --image-project=ubuntu-os-cloud --image-family=ubuntu-2004-lts
```

## Lister les VM

Pour lister toutes les VM du projet :

```bash
gcloud compute instances list
```

## Démarrer/Arrêter une VM

Pour démarrer une VM :

```bash
gcloud compute instances start NOM_VM
```

Pour arrêter une VM :

```bash
gcloud compute instances stop NOM_VM
```

## Se connecter en SSH

Pour se connecter en SSH à une VM :

```bash
gcloud compute ssh NOM_VM
```

## Supprimer une VM

Pour supprimer définitivement une VM :

```bash
gcloud compute instances delete NOM_VM
```

## Modifier une VM

Pour modifier les propriétés d'une VM existante, par exemple changer le type de machine :

```bash
gcloud compute instances set-machine-type NOM_VM --machine-type=NOUVEAU_TYPE
```

Ces commandes vous permettent de gérer l'ensemble du cycle de vie des VM sur Google Cloud Platform directement depuis la ligne de commande.