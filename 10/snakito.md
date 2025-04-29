# Projet snake
## Cahier des charges

### Description du projet
Ce projet consiste à développer une version personnalisée du célèbre jeu Snake, en utilisant le langage Python et la bibliothèque Pygame.

Le jeu doit être interactif, disposer d’une interface graphique, de sons, de règles claires, et offrir une expérience utilisateur agréable.

### Objectifs réalisables
- Implémenter la logique du jeu Snake (déplacement, collision, croissance).
- Créer une interface graphique fonctionnelle avec animations simples.
- Intégrer une bande sonore (musique et effets sonores).
- Permettre une interaction fluide via le clavier.
- Proposer un menu d’accueil et un écran de fin de partie.
- Organiser proprement le projet avec des modules séparés.
- Ajout de bonus, easter egg, autres possibilité...

### Fonctionnalités
Un menu avec différents choix de modes :

    Normal : Jeux basique sans otpions

    Automatique : Jeux basique sans avoir besoin d'être piloté

    Spécial : Ajout de fonctionnalité (étoile mario, pomme
              invincible 1 seconde, etc...)

Et un menu "HELP" qui explique comment fonctionne le jeux.

Affichage du score avec tableau de score dans le menu.

Dans l'ensemble, c'est un snake basique mais les fonctionnalité viendront avec le temps. (tout dépends les compétences de l'équipe)




### Technologies utilisées
Code :
- Python
- Pygame
- GitHub

Musique / son :
- suno.com
- youtube.com



### Nom des membres de l'équipes
- Liebe Nils
- Dénervaud Nolan
- Freigedo Roberto

### Répartition des tâches

#### 1. Gameplay & logique du jeu (Back-end Snake)

Responsable : Liebe Nils

    Mouvement du serpent (gestion des directions, du corps)

    Collision avec murs / soi-même

    Gestion de la pomme et score

    Game over / restart

    Timer, boucle principale


#### 2. Graphismes & animations

Responsable : Freigedo Roberto

    Interface graphique avec Pygame (grille, serpent, pomme, fond)

    Écran d’accueil / game over

    Animation fluide du serpent

    Choix de couleurs, éventuellement skins


#### 3. Musique & effets sonores + règles & menus

Responsable : Dénervaud Nolan

    Intégration de sons (manger, game over, musique de fond)

    Chargement de sons (format .wav ou .mp3)

    Menu principal : démarrer, quitter

    Affichage des règles, score final, meilleure performance
