# Rapport de Veille Technologique : CI/CD et Qualité Logicielle

Ce document répond aux questions de veille posées dans le cadre du projet de prédiction de la gravité des accidents routiers.

---

## Mission 1 : Comprendre CI/CD

### 1. Qu'est-ce que la CI (Continuous Integration) ?

**Définition** : L'intégration continue est une pratique de développement où les membres d'une équipe intègrent leur travail fréquemment (généralement chaque jour). Chaque intégration est vérifiée par un build automatisé et des tests pour détecter les erreurs le plus rapidement possible.

* **Quels problèmes résout-elle ?** Elle résout les conflits de code lors des fusions ("merge hell") et permet d'identifier les bugs ou les régressions immédiatement après un changement.
* **Quels sont les principes clés ?** Automatisation des builds, exécution systématique de tests à chaque commit, et maintien d'un dépôt central toujours fonctionnel.
* **Donnez 3 exemples d'outils de CI** : GitHub Actions, Jenkins et GitLab CI.



### 2. Qu'est-ce que le CD (Continuous Deployment/Delivery) ?

**Définition** : Le CD est l'extension de l'intégration continue. Il s'agit d'automatiser le processus de livraison pour que le code validé puisse être mis en production rapidement et de manière fiable.

* **Différence entre Continuous Delivery et Continuous Deployment ?** La **Continuous Delivery** (Livraison continue) garantit que le code est prêt à être déployé, mais la mise en production nécessite une validation humaine. Le **Continuous Deployment** (Déploiement continu) automatise l'envoi en production sans intervention humaine dès que les tests réussissent.
* **Quels sont les risques et bénéfices ?** Le bénéfice majeur est la rapidité de mise sur le marché. Le risque principal est de déployer une erreur si la suite de tests automatisée n'est pas assez robuste.

### 3. Pourquoi CI/CD est important ?
* **Impact sur la qualité du code** : Elle impose des standards de qualité stricts et automatiques, réduisant les erreurs humaines.
* **Impact sur la vitesse de développement** : Elle accélère les livraisons en supprimant les tâches manuelles répétitives de test et de déploiement.
* **Impact sur la collaboration en équipe** : Elle permet à l'équipe de travailler sur une base de code partagée toujours stable et validée par les outils.

---

## Mission 2 : Maîtriser uv

### 1. Qu'est-ce que uv ?
* **En quoi est-ce différent de pip/poetry/pipenv ?** uv est écrit en Rust, ce qui le rend beaucoup plus rapide. Contrairement à pip, uv centralise la gestion de Python, des environnements virtuels et des dépendances dans un seul outil.
* **Quels sont les avantages ?** Une vitesse d'exécution extrême, une gestion simplifiée des outils et une grande fiabilité grâce à son système de cache.

### 2. Comment uv fonctionne avec pyproject.toml ?
* **Structure du fichier** : Le fichier `pyproject.toml` sert de source de vérité pour déclarer les métadonnées, les dépendances et les configurations des outils.
* **Gestion des dépendances** : Les dépendances peuvent être séparées par sections (production, développement).
* **Build backend** : uv supporte des standards modernes pour préparer le package de l'application.

### 3. Comment utiliser uv dans GitHub Actions ?
* **Installation** : On utilise l'action officielle `astral-sh/setup-uv`.
* **Cache des dépendances** : uv permet de mettre en cache les bibliothèques pour accélérer les prochaines exécutions.
* **Exécution de commandes** : On lance les scripts ou les tests via `uv run`.

---

## Mission 3 : Comprendre Semantic Release

### 1. Qu'est-ce que le versionnage sémantique (SemVer) ?
* **Format MAJOR.MINOR.PATCH** : C'est une règle de numérotation standardisée.
* **Quand bumper chaque niveau ?** On augmente le **MAJOR** pour des changements cassants, le **MINOR** pour de nouvelles fonctionnalités, et le **PATCH** pour des corrections de bugs.

### 2. Qu'est-ce que Conventional Commits ?
* **Format des messages** : Les messages doivent suivre une structure précise (ex: `feat: add api route`).
* **Types de commits** : Les types comme `feat` (nouveauté) ou `fix` (correctif) indiquent la nature du changement.
* **Impact sur le versionnage** : Ces types permettent aux outils de calculer seuls le prochain numéro de version.

### 3. Comment python-semantic-release fonctionne ?
* **Configuration dans pyproject.toml** : On y définit les règles de détection des versions.
* **Génération du CHANGELOG** : L'outil rédige la liste des changements en lisant les commits.
* **Création des releases GitHub** : Il crée les tags Git et les versions sur GitHub automatiquement.

---

---

## Mission 5 : MkDocs & GitHub Pages (Bonus)

* **Comment MkDocs génère de la documentation ?** Il transforme des fichiers Markdown simples en un site web statique.
* **Comment déployer sur GitHub Pages ?** On utilise un workflow GitHub Actions qui construit le site et l'héberge.
* **Qu'est-ce que mkdocstrings ?** C'est un plugin qui extrait la documentation directement depuis les commentaires du code Python.