# Prédiction de la Gravité des Accidents Routiers (BAAC 2021-2024)

[![CI/CD Pipeline](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions/workflows/ci.yml/badge.svg)](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions/workflows/ci.yml)
[![Docker Build](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions/workflows/build.yml/badge.svg)](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/Adjaaaaaaaa/accidents_route_pr-diction/branch/main/graph/badge.svg)](https://codecov.io/gh/Adjaaaaaaaa/accidents_route_pr-diction)

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

## MCD
                 
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

## Architecture du Projet
Le projet est divisé en trois briques principales :

**ETL et Nettoyage** : Traitement massif des données brutes, gestion des valeurs manquantes et aberrantes, et ingénierie de variables.

**Modélisation ML** : Entraînement d'un modèle XGBoost multi-classe optimisé pour la détection des classes rares.

**Déploiement** : Une API REST développée avec FastAPI et une interface utilisateur sous Streamlit.

## Installation Rapide

### Prérequis
- **Python 3.11+** 
- **uv** (recommandé) ou pip
- **Docker** (optionnel)

### Installation avec uv (recommandé)
```bash
# Cloner le dépôt
git clone https://github.com/Adjaaaaaaaa/accidents_route_pr-diction.git
cd accidents_route_pr-diction

# Installer avec uv
uv sync

# Activer l'environnement
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
```

### Installation traditionnelle
```bash
# Cloner le dépôt
git clone https://github.com/Adjaaaaaaaa/accidents_route_pr-diction.git
cd accidents_route_pr-diction

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -e .
```

## Docker (Recommandé pour la production)

### Pull depuis GitHub Container Registry
```bash
# Récupérer l'image Docker
docker pull ghcr.io/adjaaaaaaaa/accidents_route_pr-diction:main

# Lancer le conteneur
docker run -p 8000:8000 ghcr.io/adjaaaaaaaa/accidents_route_pr-diction:main
```

### Build local
```bash
# Builder l'image
docker build -t accidents-api:local .

# Lancer le conteneur
docker run -p 8000:8000 accidents-api:local
```

## Pipeline de Données (ETL)
Le nettoyage s'effectue dans le notebook `etl_cleaning.ipynb`. Les étapes clés incluent :

- **Imputation par type** : Remplissage des valeurs manquantes par la médiane pour les données numériques et par le mode pour les catégories.
- **Traitement des valeurs aberrantes** : Plafonnement de la vitesse maximale autorisée à 130 km/h et de l'âge à 100 ans pour stabiliser les statistiques du modèle.
- **Feature Engineering** : Création d'interactions physiques (ex: agglo_x_vitesse, vitesse_x_collision) pour capturer les facteurs de risque majeurs.
- **Encodage** : Transformation des variables catégorielles via la méthode One-Hot Encoding (get_dummies).

## Modélisation
Le modèle final est un classificateur XGBoost entraîné dans le notebook `modelling.ipynb`.

### Stratégie de performance
- **Multi-classe** : Le modèle prédit 4 modalités distinctes.
- **Équilibrage** : Utilisation de la méthode de poids des classes équilibré (class_weight='balanced') pour compenser la rareté des accidents mortels dans le dataset.
- **Priorité opérationnelle** : Le modèle est optimisé pour maximiser le Rappel (Recall) sur la classe "Tué", afin de minimiser les faux négatifs dans les situations critiques.

## Lancement Rapide

### API FastAPI
```bash
# Lancer l'API
uv run fastapi run api/app/main.py --port 8000

# Ou avec le script dédié
uv run python api/run.py
```

**Endpoints :**
- `GET /health` - Vérification de l'état
- `POST /predict` - Prédiction de gravité
- `GET /docs` - Documentation Swagger

### Interface Streamlit
```bash
# Lancer l'interface utilisateur
uv run streamlit run Interface.py --server.port 8501
```

### Tests
```bash
# Lancer tous les tests
uv run pytest

# Tests avec couverture
uv run pytest --cov=api --cov-report=term-missing
```

## Qualité & CI/CD

Ce projet utilise une pipeline CI/CD complète :

### Checks automatiques
- **Linting** : Ruff (formatage + vérification)
- **Typage** : MyPy (vérification des types)
- **Sécurité** : Bandit (analyse statique) + Safety (dépendances)
- **Tests** : Pytest avec couverture de code
- **Pre-commit** : Qualité avant chaque commit

### Docker & Déploiement
- **Build automatique** : GitHub Actions
- **Container Registry** : GitHub Container Registry (GHCR)
- **Multi-stage build** : Images optimisées
- **Health checks** : Surveillance de santé

### Badges
![CI/CD Pipeline](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions/workflows/ci.yml/badge.svg)
![Docker Build](https://github.com/Adjaaaaaaaa/accidents_route_pr-diction/actions/workflows/build.yml/badge.svg)
![codecov](https://codecov.io/gh/Adjaaaaaaaa/accidents_route_pr-diction/branch/main/graph/badge.svg)

## Structure du Projet

```
├── api/                    # API FastAPI
│   ├── app/
│   │   ├── main.py         # Point d'entrée FastAPI
│   │   ├── models.py       # Schémas Pydantic (Entrée/Sortie)
│   │   ├── predictor.py    # Logique de prédiction et transformation
│   │   └── routes.py       # Définition des endpoints
│   ├── run.py              # Script de lancement
│   └── data_models/        # Pipeline .joblib sauvegardé
├── data/                   # Données
│   ├── raw/                # Données brutes BAAC
│   └── processed/          # Dataset nettoyé
├── notebooks/              # Notebooks d'expérimentation
│   ├── etl_cleaning.ipynb  # Pipeline ETL complet
│   └── modelling.ipynb     # Entraînement des modèles
├── tests/                  # Tests unitaires
│   └── test_api.py         # Tests de l'API
├── Interface.py            # Interface Streamlit
├── Dockerfile              # Configuration Docker
├── pyproject.toml         # Configuration du projet (uv)
├── .pre-commit-config.yaml # Hooks de qualité
└── .github/workflows/      # Pipelines CI/CD
    ├── ci.yml              # Tests et qualité
    └── build.yml           # Build Docker
```

## Contribuer

### Workflow de développement
1. **Forker** le projet
2. **Créer une branche** : `git checkout -b feature/nouvelle-fonctionnalité`
3. **Commiter** : `git commit -m "feat: ajoute nouvelle fonctionnalité"`
4. **Push** : `git push origin feature/nouvelle-fonctionnalité`
5. **Pull Request** : Vers la branche `main`

### Conventions de commits
- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `style:` Formatage (linting)
- `refactor:` Refactoring
- `test:` Tests
- `chore:` Maintenance