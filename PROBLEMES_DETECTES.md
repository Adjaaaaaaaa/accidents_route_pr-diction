# Rapport d'Audit : Problèmes de Qualité Détectés

Ce document répertorie les anomalies, dettes techniques et risques de sécurité identifiés lors de la phase de découverte du projet "Prédiction des Accidents de la Route".

## 1. Analyse Statique avec Ruff 
*Les erreurs suivantes ont été détectées automatiquement par le linter Ruff.*

1.  **F401 - Import inutilisé (`f1_score`)** : Dans `notebooks/modelling.ipynb`, le module est importé mais jamais appelé, ce qui surcharge inutilement la mémoire.
2.  **F811 - Redéfinition d'import (`classification_report`)** : Importé deux fois dans la même cellule de notebook, indiquant un manque de nettoyage du code.
3.  **F811 - Doublon de classe (`StandardScaler`)** : Redéfini à la ligne 15 après avoir été déjà importé à la ligne 10.
4.  **F401 - Import mort (`OneHotEncoder`)** : Présent dans les imports mais absent de la logique de calcul.
5.  **E402 - Import mal positionné** : Un import effectué au milieu d'une cellule de code (cellule 19), ce qui contrevient à la norme PEP 8 (les imports doivent être en tête de fichier/cellule).

## 2. Analyse de Typage avec Mypy
*Ces erreurs concernent la robustesse et la structure profonde du code.*

6.  **Conflit de noms de modules** : Mypy détecte une confusion entre `routes` et `app.routes`, signalant une structure de dossiers ambiguë pour Python.
7.  **Absence de fichiers `__init__.py`** : Les dossiers `api/` et `app/` ne sont pas reconnus comme des packages officiels, risquant de briser les imports lors du déploiement.
8.  **Missing Library Stubs (`pandas`)** : Mypy ne peut pas vérifier les types pour Pandas car les "stubs" (fichiers de définition) ne sont pas installés.
9.  **Missing Library Stubs (`joblib`)** : Impossible de garantir que le chargement du modèle `.joblib` est sécurisé au niveau des types.
10. **Missing Library Stubs (`requests`)** : Dans `Interface.py`, les appels API ne sont pas protégés par une vérification de type, augmentant le risque de crash à l'exécution.
11. **Import-not-found (`app.routes`)** : L'analyseur ne parvient pas à localiser physiquement la source des routes depuis `main.py`.

## 3. Sécurité et Configuration
12. **Configuration inscrite en dur** : L'URL de l'API et les paramètres de déploiement sont inscrits directement dans le code source (ex: Interface.py). L'absence d'un fichier de configuration environnementale (.env) rend le passage du mode "développement" au mode "production" complexe et sujet à des erreurs manuelles.
13. **Permissions CI/CD excessives** : Le workflow GitHub Actions possède des droits d'écriture globaux qui devraient être restreints au strict nécessaire.
14. **Absence de `.gitignore` complet** : Des fichiers sensibles ou inutiles (comme `__pycache__` ou `.venv`) pourraient être poussés par erreur sur le dépôt distant.

## 4. Documentation et Maintenance 
15. **Docstrings manquantes** : Les fonctions de prédiction dans `predictor.py` n'ont pas de commentaires explicatifs `""" ... """`.
16. **Annotations de types absentes** : Les signatures de fonctions dans `main.py` n'indiquent pas les types d'entrée ni de sortie (ex: `-> dict`).
17. **README incomplet** : Le fichier de présentation n'explique pas comment configurer les variables d'environnement pour faire fonctionner l'interface Streamlit.

## 5. Architecture et Code Mort 
18. **Absence de tests unitaires** : Aucun framework de test (`pytest`) n'est configuré pour valider la précision du modèle avant le déploiement.
19. **Versions de dépendances "floues"** : Dans `pyproject.toml`, l'utilisation de `>=` au lieu de versions fixées (`==`) peut entraîner des ruptures de compatibilité lors de futures mises à jour.
20. **Gestion d'erreurs inexistante** : Manque de blocs `try...except` dans `Interface.py` pour gérer les cas où l'API FastAPI est injoignable.