# Projet de Prédiction de la Gravité des Accidents Routiers (BAAC 2021-2024)
Projet de Prédiction de la Gravité des Accidents Routiers (BAAC 2021-2024)
Ce projet utilise les données ouvertes du gouvernement français (fichiers BAAC) pour prédire la gravité des accidents de la route. L'objectif est de fournir un outil d'aide à la décision capable d'estimer en temps réel la probabilité qu'un accident appartienne à l'une des quatre classes de gravité : Indemne, Tué, Grave ou Léger.

## MCD
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


## Architecture du Projet
Le projet est divisé en trois briques principales :

ETL et Nettoyage : Traitement massif des données brutes, gestion des valeurs manquantes et aberrantes, et ingénierie de variables.

Modélisation ML : Entraînement d'un modèle XGBoost multi-classe optimisé pour la détection des classes rares.

Déploiement : Une API REST développée avec FastAPI et une interface utilisateur sous Streamlit.

## Installation et Configuration
* Prérequis
Python 3.10 ou supérieur

Environnement virtuel recommandé

* Installation
Cloner le dépôt :

Bash
git clone https://github.com/Adjaaaaaaaa/accidents_route_pr-diction.git

Installer les dépendances :

Bash
pip install -r requirements.txt
Pipeline de Données (ETL)
Le nettoyage s'effectue dans le notebook etl_cleaning.ipynb. Les étapes clés incluent :

Imputation par type : Remplissage des valeurs manquantes par la médiane pour les données numériques et par le mode pour les catégories.

Traitement des valeurs aberrantes : Plafonnement de la vitesse maximale autorisée à 130 km/h et de l'âge à 100 ans pour stabiliser les statistiques du modèle.

Feature Engineering : Création d'interactions physiques (ex: agglo_x_vitesse, vitesse_x_collision) pour capturer les facteurs de risque majeurs.

Encodage : Transformation des variables catégorielles via la méthode One-Hot Encoding (get_dummies).

## Modélisation
Le modèle final est un classificateur XGBoost entraîné dans le notebook modelling.ipynb.

### Stratégie de performance
Multi-classe : Le modèle prédit 4 modalités distinctes.

Équilibrage : Utilisation de la méthode de poids des classes équilibré (class_weight='balanced') pour compenser la rareté des accidents mortels dans le dataset.

Priorité opérationnelle : Le modèle est optimisé pour maximiser le Rappel (Recall) sur la classe "Tué", afin de minimiser les faux négatifs dans les situations critiques.

## Déploiement
Lancement de l'API (FastAPI)
L'API charge le pipeline complet (incluant le StandardScaler) et expose un point d'entrée pour la prédiction.

Bash
python api/run.py
Vérification de l'état : GET /health

Prédiction : POST /predict

Lancement de l'Interface (Streamlit)
L'interface permet une saisie simplifiée des caractéristiques de l'accident via des formulaires.

Bash
streamlit run Interface.py
Interprétation des résultats
L'application renvoie un détail des probabilités pour chaque modalité :

Probabilité : Indique le score de confiance du modèle pour chaque classe lors d'une prédiction spécifique.

# Structure des dossiers
```
├── api/
│   ├── app/
│   │   ├── main.py        # Point d'entrée FastAPI
│   │   ├── models.py      # Schémas Pydantic (Entrée/Sortie)
│   │   ├── predictor.py   # Logique de prédiction et transformation
│   │   └── routes.py      # Définition des points d'accès
│   └── data_models/       # Pipeline .joblib sauvegardé
├── data/
│   ├── raw/               # Données brutes BAAC
│   └── processed/         # Dataset nettoyé
├── notebooks/             # Notebooks d'expérimentation
└── Interface.py           # Code de l'interface Streamlit
```