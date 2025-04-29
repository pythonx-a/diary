# 📝 Cahier des charges – Application "Classement Jeux Étudiants"

## 🎯 Objectif

Développer une **application web** permettant de gérer et d’afficher un **classement général d’équipes étudiantes** sur différents jeux (Babyfoot, Billard, Beer Pong, Mario Kart, etc.), avec un **système ELO** pour classer les performances.
L'application permet à chaque joueur de se créer un compte, de former une équipe, d'enregistrer les résultats des matchs, et de visualiser les classements sur un écran dans un local étudiant.

## 🧑‍💻 Utilisateurs

### Joueurs
- Peuvent créer un compte (`pseudo`, `mot de passe`)
- Peuvent recevoir une invitation à rejoindre une équipe
- Peuvent se connecter à leur compte joueur

### Équipes
- Formées de **2 joueurs maximum**
- Créées par un joueur en invitant un autre
- Doivent être **validées** par le joueur invité
- Peuvent se connecter avec :
  - **Nom de l’équipe**
  - **Mot de passe de l’un des deux joueurs**

## 🔐 Authentification

### Connexion joueur :
- `pseudo + mot de passe`

### Connexion équipe :
- `nom de l’équipe + mot de passe` du **joueur 1 ou 2**

## 🔨 Fonctionnalités principales

### 1. Création d’un compte joueur
- Interface d’inscription (pseudo unique + mot de passe)

### 2. Création d’une équipe
- Un joueur invite un autre à rejoindre son équipe
- L’équipe a un **nom unique**
- Le joueur invité **valide** via son espace personnel
- Une fois les deux joueurs validés → équipe activée

### 3. Ajout d’un match
- **Jeux 1v1 ou FFA** : L'enregistrement du match se fait depuis **l’espace JOUEUR**
  - Authentification via `pseudo + mot de passe`
  - Sélectionner le jeu et le format (1v1 ou FFA)
  - Renseigner les autres joueurs adverses et le score
  - L'autre joueur **doit valider** pour finaliser le match

- **Jeux 2v2** : L'enregistrement du match se fait depuis **l’espace ÉQUIPE**
  - Authentification via `nom d’équipe + mot de passe` (joueur 1 ou joueur 2)
  - Sélectionner le jeu et le format (2v2)
  - Recherche l’équipe adverse
  - Renseigner le score
  - L’équipe adverse **doit valider** pour finaliser le match

### 4. Validation du match
- L’équipe adverse ou le joueur adverse peut :
  - **Accepter** → mise à jour du classement ELO
  - **Refuser** → match annulé
- Si refus : message d’erreur/justification possible (optionnel)

### 5. Classements
- Classement **par jeu** et **par format** (ex : Babyfoot 1v1 ≠ 2v2)
- Affichage :
  - Classements actuels
  - Historique des matchs
  - Statistiques (optionnel)

### 6. Affichage sur un écran
- Page dédiée pour un écran dans le local étudiant :
  - Classements dynamiques
  - Matchs récents

## 🎮 Jeux gérés

| Jeu              | Formats possibles     |
|------------------|------------------------|
| Babyfoot         | 1v1, 2v2               |
| Billard          | 1v1, 2v2               |
| Beer Pong        | 1v1, 2v2               |
| Mario Kart       | FFA (Free For All)     |
| Super Smash Bros | FFA                    |

Les formats sont modulables et extensibles par l’admin.

## 📈 Système de classement

### Système ELO :
- Score initial : 1000 points
- Calcul basé sur la différence entre les scores des deux équipes
- Un classement distinct est stocké pour chaque **jeu + format**

### Exemple :
- Équipe A vs Équipe B → score saisi → confirmation → score ELO mis à jour pour les deux

## 🛠️ Architecture technique

### Backend
- **Python + Flask**
- **SQLAlchemy** pour ORM (modèles, base de données)
- Base : **SQLite** (ou PostgreSQL si hébergement)

### Frontend
- HTML/Jinja2 (ou API Flask + React en option)
- Interface responsive compatible mobile

### Authentification
- Gestion sécurisée avec hashage de mots de passe (`werkzeug.security`)

### Affichage télé
- Route spéciale `/screen` avec auto-refresh des classements
