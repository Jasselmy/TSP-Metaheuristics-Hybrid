# Hybridation de Métaheuristiques pour le Problème du Voyageur de Commerce

## Présentation du projet

L'objectif du projet est d'étudier et d'implémenter différentes méthodes heuristiques et métaheuristiques pour résoudre le **problème du voyageur de commerce (Traveling Salesman Problem - TSP)**, puis de proposer une **approche hybride** combinant plusieurs algorithmes.

Le projet comprend :

* l’implémentation de plusieurs algorithmes heuristiques et métaheuristiques
* une approche d’**hybridation**
* des expérimentations sur différentes instances
* une comparaison des performances
* un rapport scientifique rédigé en **LaTeX**

------

## Problème du voyageur de commerce

Le **Traveling Salesman Problem (TSP)** consiste à trouver le **plus court circuit** passant par un ensemble de villes exactement une fois et revenant à la ville de départ.

Soit :

* un ensemble de villes
  [
  V = {1,2,\dots,n}
  ]

* une matrice de distances

[
D = (d_{ij})
]

où (d_{ij}) représente la distance entre la ville (i) et la ville (j).

L'objectif est de déterminer une permutation des villes minimisant la distance totale du tour.

Le TSP est un problème **NP-difficile**, ce qui rend l'utilisation de **métaheuristiques particulièrement pertinente** pour obtenir des solutions de bonne qualité.

------

## Méthodes implémentées

### Heuristique gloutonne (Plus proche voisin)

Cette heuristique construit progressivement une tournée en choisissant à chaque étape la **ville non visitée la plus proche**.

Avantages :

* très rapide
* simple à implémenter

Limites :

* peut produire des solutions éloignées de l’optimal.

------

### Threshold Accepting

L'algorithme **Threshold Accepting** est une métaheuristique proche du recuit simulé.

Il accepte une solution moins bonne si la dégradation de la fonction objectif ne dépasse pas un **seuil donné**.

Ce seuil diminue progressivement au cours de l'algorithme.

Cette stratégie permet d'éviter de rester bloqué dans un **minimum local**.

------

### Recuit simulé (Simulated Annealing)

Le **recuit simulé** est inspiré d’un processus physique de refroidissement des métaux.

Une solution moins bonne peut être acceptée avec une probabilité donnée par :

[
P = e^{-\Delta/T}
]

où :

* (T) représente la température
* (\Delta) la variation de la fonction objectif.

Lorsque la température diminue, l’algorithme devient plus sélectif.

------

### Hybridation proposée

Afin d'améliorer les performances, nous proposons une **approche hybride** combinant plusieurs méthodes.

La stratégie adoptée est la suivante :

1. génération d’une solution initiale par l’heuristique gloutonne
2. amélioration de la solution par **Threshold Accepting**
3. optimisation finale par **recuit simulé**

Cette hybridation permet de combiner :

* la rapidité d'une heuristique constructive
* l'efficacité de la recherche locale
* la capacité d'exploration globale des métaheuristiques.

------

## Structure du projet

```
TSP-Metaheuristics-Hybrid
  data
     instance_29.txt
     instance_51.txt

 src
     reader.py
     tsp_utils.py
     greedy.py
     threshold_accepting.py
     simulated_annealing.py
     hybrid_metaheuristic.py
     experiments.py

  results
     figures
     tables

   report
     report.tex
     requirements.txt

  README.md


## Installation

Cloner le dépôt :

```
git clone https://github.com/jasselmy/TSP-Metaheuristics-Hybrid.git
cd TSP-Metaheuristics-Hybrid
```

Installer les dépendances :

```
pip install -r requirements.txt
```

---

## Exécution des expériences

Pour lancer les expérimentations :

```
python src/experiments.py
```

Le script va :

* charger les instances du TSP
* exécuter les différentes métaheuristiques
* comparer les résultats obtenus.

---

## Résultats expérimentaux

Les algorithmes sont comparés selon :

* la **distance totale de la tournée**
* le **temps d'exécution**

Exemple de résultats :

| Méthode             | Distance | Temps (s) |
| ------------------- | -------- | --------- |
| Greedy              | 2760     | 0.01      |
| Threshold Accepting | 2410     | 0.35      |
| Simulated Annealing | 2300     | 0.60      |
| Hybrid              | **2200** | 0.70      |

L’approche hybride permet généralement d’obtenir les **meilleures solutions**.

---

## Technologies utilisées

* Python
* NumPy
* Matplotlib
* LaTeX

---

## Rapport

Un rapport détaillé présentant :

* la formulation du problème
* les algorithmes utilisés
* la stratégie d’hybridation
* les résultats expérimentaux

est disponible dans le dossier :

```
report/
```

Compilation du rapport :

```
pdflatex report.tex
```


## Perspectives

Plusieurs améliorations sont possibles :

* utilisation d’algorithmes génétiques
* colonie de fourmis (Ant Colony Optimization)
* recherche tabou
* opérateurs de voisinage avancés (**2-opt**, **3-opt**)


## Auteur
Yasmine El Alamy
Étudiante en Master
**Intelligence Artificielle et Recherche Opérationnelle**

---

## Licence

Projet réalisé dans un cadre **académique universitaire**.
