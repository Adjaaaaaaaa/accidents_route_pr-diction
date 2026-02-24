# Prédiction de la Gravité des Accidents Routiers

> Projet de Machine Learning pour prédire la gravité des accidents de la route en utilisant les données BAAC françaises (2021-2024).

## Objectif

Fournir un outil d'aide à la décision capable d'estimer en temps réel la probabilité qu'un accident appartienne à l'une des quatre classes de gravité :
- **Indemne** 
- **Tué**
- **Grave** 
- **Léger**

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   ETL & Data    │    │   ML Models    │    │   Deployment    │
│   Processing    │───▶│   Training      │───▶│   & API         │
│                 │    │                 │    │                 │
│ • Nettoyage     │    │ • XGBoost      │    │ • FastAPI       │
│ • Feature Eng   │    │ • Multi-classe  │    │ • Docker        │
│ • Validation    │    │ • Optimisation  │    │ • CI/CD         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Démarrage Rapide

### Prérequis
- **Python 3.11+** 
- **uv** (recommandé) ou pip
- **Docker** (optionnel)

### Installation avec uv
```bash
# Cloner le dépôt
git clone https://github.com/Adjaaaaaaaa/accidents_route_pr-diction.git
cd accidents_route_pr-diction

# Installer avec uv
uv sync

# Lancer l'API
uv run fastapi run api/app/main.py --port 8000
```

### Docker
```bash
# Récupérer l'image
docker pull ghcr.io/adjaaaaaaaa/accidents_route_pr-diction:main

# Lancer le conteneur
docker run -p 8000:8000 ghcr.io/adjaaaaaaaa/accidents_route_pr-diction:main
```

## Modèle de Données

### MCD (Modèle Conceptuel de Données)

```                 
       |         LIEUX         |                    |   CARACTERISTIQUES    |
       +-----------------------+                    +-----------------------+
       | Num_Acc (PK, FK)      |<-------------------| Num_Acc (PK)          |
       | catr, voie, v1, v2    |      (1,1)         | jour, mois, an, hrmn  |
       | circ, nbv, vosp, prof |      DÉCRIT        | lum, atm, col         |
       | pr, pr1, plan, lartpc |                    | dep, com, agg, int    |
       | larrout, surf, infra  |                    | adr, lat, long        |
       | situ, vma             |                    |                       |
       +-----------------------+                    +-----------------------+
                                                               |
                                                               | (1,n)
                                                               |
                                                          +----V----+
                                                          |IMPLIQUER|
                                                          +----V----+
                                                               |
                                                               | (1,1)
                                                               |
       +-----------------------+                    +----------V------------+
       |        USAGERS        |                    |       VEHICULES       |
       +-----------------------+                    +-----------------------+
       | id_usager (PK)        |      (1,1)         | id_vehicule (PK)      |
       | Num_Acc (FK)          |<-------------------| Num_Acc (FK)          |
       | id_vehicule (FK)      |      OCCUPER /     | num_veh               |
       | num_veh, place, catu  |       HEURTER      | senc, catv, motor     |
       | grav (CIBLE), sexe    |                    | obs, obsm, choc       |
       | an_nais, trajet, secu |      (1,n)         | manv, occutc          |
       | locp, actp, etatp     |                    |                       |
       +-----------------------+                    +-----------------------+
```

## Modélisation

Le modèle final est un classificateur **XGBoost** entraîné pour prédire la gravité des accidents.

### Stratégie de performance
- **Multi-classe** : Prédiction des 4 modalités (Indemne, Tué, Grave, Léger)
- **Équilibrage** : Poids des classes équilibrés pour gérer les déséquilibres
- **Optimisation** : Maximisation du Rappel sur la classe "Tué"

## Pipeline ETL

Le nettoyage s'effectue dans le notebook `etl_cleaning.ipynb` :

- **Imputation par type** : Médiane pour numériques, mode pour catégories
- **Traitement des valeurs aberrantes** : Plafonnement vitesse (130 km/h) et âge (100 ans)
- **Feature Engineering** : Interactions physiques pour capturer les risques
- **Encodage** : One-Hot Encoding pour variables catégorielles

## Endpoints API

### Health Check
```bash
curl http://localhost:8000/health
```

### Prédiction
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 25, "vitesse": 50, "nb_voies": 2}'
```

### Documentation Interactive
- **Swagger UI** : `http://localhost:8000/docs`
- **ReDoc** : `http://localhost:8000/redoc`

## Tests

```bash
# Lancer tous les tests
uv run pytest

# Tests avec couverture
uv run pytest --cov=api --cov-report=term-missing
```

## Structure du Projet

```
├── api/                    # API FastAPI
│   ├── app/
│   │   ├── main.py         # Point d'entrée FastAPI
│   │   ├── models.py       # Schémas Pydantic
│   │   ├── predictor.py    # Logique de prédiction
│   │   └── routes.py       # Endpoints
│   └── run.py              # Script de lancement
├── data/                   # Données
├── notebooks/              # Notebooks d'expérimentation
├── tests/                  # Tests unitaires
├── Dockerfile              # Configuration Docker
├── pyproject.toml         # Configuration du projet
└── .github/workflows/      # Pipelines CI/CD
```

## Liens Utiles

- **GitHub Repository** : [accidents_route_pr-diction](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction)
- **CI/CD Pipeline** : [GitHub Actions](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions)
- **Docker Image** : [GitHub Container Registry](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/pkgs/container/accidents_route_pr-diction)

---

**Prédissons ensemble des routes plus sûres**