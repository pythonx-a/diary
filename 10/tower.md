# Plan du Projet : Jeu de Tower Defense

## Description du Projet
L'objectif est de créer un **jeu de Tower Defense** en Python où le joueur place des tours sur une grille pour empêcher des vagues d'ennemis d'atteindre une destination. Les ennemis suivent un chemin prédéfini, et les tours attaquent automatiquement. Le joueur gagne de l'argent en éliminant les ennemis pour acheter ou améliorer ses tours. Le jeu sera simple mais captivant, avec des possibilités d'ajouter des mécaniques créatives comme la destruction d'éléments de la carte (ex. casser des ponts pour bloquer les ennemis). Le projet est conçu pour être réalisé en 6 semaines, en équilibrant un gameplay de base avec des améliorations amusantes, adapté à un niveau intermédiaire en Python.

## Objectifs Réalisables
- **Gameplay de base** : Implémenter un jeu de tower defense fonctionnel avec une grille, des vagues d'ennemis, et des tours placées qui attaquent automatiquement.
- **Interaction du joueur** : Permettre au joueur de placer, améliorer ou vendre des tours avec un système de monnaie gagné en battant les ennemis.
- **Difficulté progressive** : Introduire des vagues d'ennemis qui augmentent en vitesse, en santé ou en nombre au fil du temps.
- **Interface utilisateur** : Créer un affichage clair avec une grille, un score, un compteur d'argent, et des menus pour gérer les tours (placement, upgrade).
- **Polissage** : Ajouter des graphismes simples (sprites ou formes), des sons, et un écran de menu/game over.
- **Mécanique originale** : Intégrer au moins une fonctionnalité unique, comme la possibilité de casser des ponts pour bloquer les ennemis.

## Fonctionnalités
### Fonctionnalités de base
- **Grille de jeu** : Une carte sous forme de grille (ex. 10x10 ou 15x10) avec un chemin prédéfini pour les ennemis.
- **Tours** :
  - Placement par clic sur la grille (si la case est libre et que le joueur a assez d'argent).
  - Attaque automatique des ennemis à portée (ex. rayon de 3 cases).
  - Types de tours : ex. tour de base (dégâts moyens), tour rapide (faibles dégâts, cadence élevée).
- **Ennemis** :
  - Apparition en vagues (ex. 5 ennemis à la vague 1, 10 à la vague 3).
  - Caractéristiques : santé, vitesse, récompense en argent à leur mort.
  - Suivent un chemin fixe défini dans la carte.
- **Système de monnaie** : Gagner de l'argent en tuant des ennemis, utilisé pour acheter/mettre à jour des tours.
- **Interface** :
  - Affichage de la grille, des tours, des ennemis, du score, et de l'argent.
  - Menu pour choisir les tours à placer ou améliorer.
  - Écran de démarrage et de game over (avec option de rejouer).
- **Conditions de victoire/défaite** :
  - Défaite si trop d'ennemis atteignent la destination (ex. 10 ennemis passent).
  - Victoire après avoir survécu à un nombre défini de vagues (ex. 20 vagues).

### Fonctionnalités avancées (améliorations)
- **Casser des ponts** :
  - Certaines cases du chemin sont des "ponts" que le joueur peut détruire (via un coût en argent).
  - Une fois cassé, le pont bloque le chemin, forçant les ennemis à prendre un autre chemin (donc de revenir en arrière et passer par un autre chemin).
  - Exemple : un pont sur une rivière qui, une fois détruit, empêche les ennemis de passer.
- **Améliorations des tours** :
  - Chaque tour peut être améliorée (ex. +50% de dégâts ou +1 case de portée) pour un coût.
  - Optionnel : arbre d’améliorations (ex. choisir entre dégâts ou portée).
- **Types d’ennemis variés** :
  - Ennemi rapide (faible santé, vitesse élevée).
  - Ennemi tank (haute santé, lent).
  - Ennemi volant (ignore certains obstacles, nécessite une tour spéciale).
- **Obstacles dynamiques** :
  - En plus des ponts, ajouter des murs temporaires que le joueur peut poser pour ralentir les ennemis.
  - Exemple : un mur qui bloque une case pendant 5 secondes.
- **Power-ups** :
  - Objets temporaires sur la carte (ex. bonus d’argent, gel des ennemis).
  - Exemple : une bombe qui inflige des dégâts de zone à tous les ennemis à l’écran.
- **Boss** :
  - Une vague spéciale avec un ennemi très résistant (ex. 10x la santé d’un ennemi normal).
  - Récompense élevée si vaincu.
- **Chemins multiples** :
  - La carte peut avoir plusieurs chemins que les ennemis choisissent aléatoirement.
  - Casser un pont peut forcer les ennemis à prendre un chemin plus long.
- **Sauvegarde des scores** :
  - Enregistrer les meilleurs scores (ex. nombre de vagues survécues) dans un fichier JSON.
- **Niveaux** :
  - Plusieurs cartes avec des chemins différents (ex. une carte avec un pont, une autre avec des virages serrés).
  - Optionnel : éditeur de carte simple où le joueur dessine le chemin.

### Idées créatives
- **Thème narratif** :
  - Ex. une forteresse médiévale (tours = archers, ennemis = orcs) ou une base spatiale (tours = lasers, ennemis = aliens).
  - Ajoute des sprites et sons thématiques (ex. cris d’orcs, zaps de lasers).
- **Tours spéciales** :
  - Tour de ralentissement (réduit la vitesse des ennemis dans une zone).
  - Tour de soutien (augmente les dégâts des tours voisines).
- **Mode infini** :
  - Après la dernière vague, les ennemis continuent avec une difficulté croissante pour tester l’endurance du joueur.

## Technologies Utilisées
- **Python** : Langage principal pour coder la logique du jeu.
- **Pygame** :
  - Gestion de l’affichage (grille, sprites, texte).
  - Détection des clics pour placer des tours.
  - Sons (effets pour tirs, destructions, etc.).
- **JSON ou TXT (optionnel)** :
  - Pour sauvegarder les scores ou définir les cartes (ex. chemin des ennemis sous forme de liste de coordonnées).
- **Sprites et sons** :
  - Sprites gratuits sur OpenGameArt.org (ex. tours, ennemis).
  - Sons libres sur Freesound.org (ex. tirs, explosions).
- **Éditeur** :
  - VSCode
- **Modules Python standards** :
  - `random` pour la génération aléatoire (placement des ennemis, power-ups).
  - `math` pour les calculs de distance (portée des tours).
  - `json` pour les sauvegardes.

## Plan sur 6 Semaines
- **Semaine 1 : Setup et base**
  - Installer Pygame, créer une fenêtre avec une grille (ex. rectangles pour cases).
  - Afficher une tour fixe qui tire sur un ennemi test (carré qui bouge).
- **Semaine 2 : Ennemis et chemin**
  - Implémenter un chemin prédéfini (liste de coordonnées).
  - Ajouter des ennemis qui apparaissent en vagues et suivent le chemin.
  - Gérer les collisions tour/ennemi (ennemi perd de la santé).
- **Semaine 3 : Système de jeu**
  - Ajouter un système d’argent (gain à la mort des ennemis).
  - Permettre le placement de tours par clic (si assez d’argent).
  - Implémenter la condition de défaite (ex. ennemis qui passent).
- **Semaine 4 : Améliorations**
  - Ajouter la mécanique de ponts cassables (clic pour détruire, chemin bloqué).
  - Implémenter une amélioration de tour (ex. +dégâts pour un coût).
  - Ajouter un type d’ennemi différent (ex. plus rapide).
- **Semaine 5 : Interface et polissage**
  - Créer un menu principal (jouer/quitter) et un écran de game over.
  - Ajouter des sprites (tours, ennemis) et sons (tirs, destructions).
  - Afficher l’argent, le score, et la vague en cours.
- **Semaine 6 : Finalisation**
  - Tester pour corriger les bugs (ex. ennemis qui passent à travers, tours mal placées).
  - Ajouter une fonctionnalité bonus (ex. power-up, boss, sauvegarde des scores).
  - Présentation du projet devant la classe
