# Mission 4 : Comparatif des outils de Qualité Code

L'objectif de cette étude est de comparer les outils de validation de code afin de structurer une chaîne de qualité robuste pour le projet "Accidents de la Route".

## 1. Linters et Formatters Python

Le linter analyse le code pour détecter des erreurs de logique ou des oublis, tandis que le formatter s'occupe de la mise en page automatique (espaces, retours à la ligne).

| Outil | Catégorie | Avantages | Inconvénients | Choix |
| :--- | :--- | :--- | :--- | :--- |
| **Ruff** | Linter & Formatter | Extrêmement rapide, remplace plusieurs outils anciens, configuration simplifiée. | Outil plus récent que ses concurrents historiques. | **Oui** |
| **Flake8** | Linter | Très stable et largement utilisé par la communauté. | Nécessite l'installation de nombreux plugins pour être complet. | Non |
| **Pylint** | Linter | Analyse très profonde et détaillée du code. | Très lent et peut générer beaucoup de messages d'alerte inutiles. | Non |
| **Black** | Formatter | Propose un style unique et automatique très populaire. | Moins rapide que les outils modernes écrits en Rust. | Non |
| **autopep8** | Formatter | Plus souple dans l'application des règles de style. | Moins rigoureux que Black pour garantir l'uniformité du code. | Non |

**Justification :** Le choix de **Ruff** est motivé par sa rapidité et sa capacité à centraliser le linting et le formatage dans un seul outil. Cela simplifie la gestion du projet et accélère les vérifications automatiques lors du développement.

---

## 2. Type Checkers (Vérification des types)

Le typage permet de s'assurer que les données manipulées (nombres, textes, listes) correspondent bien à ce que le programme attend, ce qui évite des bugs invisibles.

| Outil | Précision | Vitesse | Intégration avec l'éditeur (IDE) | Choix |
| :--- | :--- | :--- | :--- | :--- |
| **Mypy** | Référence | Moyen | Bien intégré dans la plupart des éditeurs. | **Oui** |
| **Pyright** | Excellente | Très rapide | Intégration parfaite dans VS Code (via Pylance). | Non |
| **Pyre** | Bonne | Rapide | Plus difficile à configurer pour un petit projet. | Non |

**Justification :** **Mypy** est sélectionné car c'est l'outil de référence pour le typage en Python, avec une maturité éprouvée et une compatibilité excellente avec les projets existants. Il offre un bon équilibre entre précision et stabilité.

---

## 3. Frameworks de Tests

Le framework de tests sert à vérifier que chaque fonction ou calcul du projet produit bien le résultat attendu.

| Outil | Facilité d'utilisation | Écosystème (Plugins) | Style d'écriture | Choix |
| :--- | :--- | :--- | :--- | :--- |
| **pytest** | Élevée | Très riche et varié | Simple, basé sur des fonctions classiques. | **Oui** |
| **unittest** | Modérée | Limité | Plus rigide, basé sur une structure de classes. | Non |

**Justification :** **pytest** est privilégié pour sa simplicité et sa flexibilité. Il permet de créer rapidement des tests fiables, particulièrement adaptés aux scripts de traitement de données.

---

## 4. Security Scanners (Analyse de sécurité)

| Outil | Fonction | Utilité pour le projet | Choix |
| :--- | :--- | :--- | :--- |
| **Bandit** | Analyse du code | Détecte les erreurs de programmation qui pourraient être dangereuses. | **Oui** |
| **Safety** | Dépendances | Vérifie si les bibliothèques installées présentent des failles connues. | **Oui** |

---

## Synthèse du choix technique

Pour ce projet, la suite d'outils suivante est adoptée :
* **Ruff** : Pour la propreté et le formatage du code.
* **Mypy** : Pour la sécurité des types de données.
* **pytest** : Pour la validation du bon fonctionnement du code.
* **Bandit & Safety** : Pour la sécurité globale.