# rpnCalulatrice

Ce projet est une API de calculatrice utilisant la notation polonaise inverse (NPI) implémentée avec FastAPI et déployée avec Docker.

## Prérequis

Assurez-vous d'avoir installé sur votre machine :

- Docker
- Docker Compose

## Configuration initiale

1. Clonez le dépôt de l'application sur votre machine locale :

```bash
git clone https://github.com/saravalencia/rpnCalulatrice.git
cd npiCalculatrice
```

2. Construisez l'image Docker :

```bash
docker-compose build
```

3. Démarrage de l'application

```bash
docker-compose up
```
Cette commande lancera l'application et la rendra accessible à l'adresse http://localhost:8000

## Utilisation de l'API

Une fois l'application démarrée, vous pouvez l'utiliser pour effectuer des calculs en notation polonaise inverse via l'endpoint /calculate.

### Endpoint /calculate

Envoyez une requête POST à cet endpoint avec un corps de requête JSON contenant l'expression à évaluer. Par exemple :

```bash
{
  "expression": "3 4 +"
}
```

### Téléchargement des données en CSV

Pour télécharger un fichier CSV contenant l'historique des calculs, envoyez une requête GET à /download-csv. Le fichier CSV sera téléchargé localement.