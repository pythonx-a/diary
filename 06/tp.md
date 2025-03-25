# 🐍 Travail Pratique – Durée : 90 minutes  

## Thème : Gestion de créatures magiques 🧙‍♂️🐉

### 🎯 Objectifs pédagogiques

- Comprendre et appliquer l'héritage en Python
- Savoir surcharger des opérateurs (`__str__`, `__add__`, `__eq__`, etc.)
- Utiliser efficacement l’autoreload dans un environnement IPython
- Structurer son code avec des classes modulaires

### 📦 Contexte

Vous travaillez pour l’Académie des Sciences Magiques. Le professeur Datalore vous demande de créer un module de gestion de **créatures magiques**. Chaque créature a des caractéristiques et peut interagir avec d'autres créatures. Vous devez aussi faciliter le développement avec l’autoreload d’IPython.

### 🧩 Étapes à suivre

#### 1. Mise en place de l’environnement (5 min)

Dans un notebook Jupyter :

```python
%load_ext autoreload
%autoreload 2
```

Créer un fichier Python `creatures.py` que vous allez importer et modifier pendant tout le TP.

#### 2. Classe de base : `Creature` (15 min)

Créez une classe `Creature` avec :

- attributs : `nom`, `force`, `vie`
- méthode `__str__` pour afficher proprement la créature
- méthode `is_alive()` qui retourne `True` si la créature a encore de la vie

Exemple attendu :

```python
>>> print(c)
🌟 Nom: Griffon | Force: 12 | Vie: 40
```

#### 3. Héritage : créatures spécifiques (15 min)

Créez deux classes héritées :

- `Dragon(Creature)`  
  - Ajoutez un attribut `feu=True`
  - Surchargez `__str__` pour ajouter 🔥

- `Licorne(Creature)`  
  - Ajoutez un attribut `magie=100`
  - Méthode spéciale `soin()` qui augmente sa propre vie de 10

#### 4. Surcharge d’opérateur : duel magique (25 min)

Implémentez dans `Creature` la méthode `__add__` :

```python
def __add__(self, other):
    # retourne une nouvelle créature issue de la fusion
```

Exemple :

```python
c1 = Dragon("Smaug", 20, 100)
c2 = Licorne("Luna", 10, 80)
fusion = c1 + c2
print(fusion)
# Nom: Smaug-Luna | Force: 30 | Vie: 180
```

Ajoutez aussi la surcharge de `__eq__` : deux créatures sont égales si elles ont le même nom **et** la même force.

Définir `__hash__` pour que la condition d'égalité soit respectée.

#### 5. Combat

- Surcharge de `__lt__` pour comparer les créatures par force
- Implémenter un combat simple : une méthode `attaquer(cible)` qui retire `self.force // 2` à la vie de la cible
- Sauvegarder une liste de créatures dans un fichier JSON

### ✅ Critères de réussite

- Code bien structuré, clair, avec commentaires
- Bonne utilisation de l’héritage
- Surcharge d’opérateurs correcte et utile
- Utilisation de `%autoreload` fonctionnelle pendant le développement

### 🧠 Conseil

Travaillez par petits fichiers et testez au fur et à mesure.