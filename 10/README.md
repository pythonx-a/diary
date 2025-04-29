# Semaine 10/16

- [x] Correction Quiz Q01
- [ ] Regex (suite)
- [ ] ABC
- [ ] Cahier des charges mini projets
- [ ] Mini-projet

## Correction du Quiz QZ-01

1. BDFL: Benevolent Dictator For Life
2. REPL: Read-Eval-Print Loop
3. ipython
4. Syntaxe
   1. `[1]` liste
   2. `{1}` set
   3. `{1:2}` dictionnaire
   4. `(1,2)` tuple (liste immuable)
   5. `(i for i in range(3))` générateur   
   6. `'abc'` chaîne de caractères
5. Un décorateur c'est : permet d'encapsuler une fonction dans une autre
6. Importer `sqrt`: `from math import sqrt`
7. Le type d'une variable est déterminé automatiquement ua moment de l'exécution
8. `__init__` est le *constructeur* de la classe
9. Duck Typing, un itérateur contient : `__iter__` et `__next__`
10. CLI: Command Line Interface, on peut utiliser `Click`.
11. Méthodes: actions, Attributs: données
12. `yield`
13. `self` est une convention pour référencer l'instance de la classe actuelle dans une méthode.
14. `next` est utilisé pour obtenir le prochain élément d'un itérateur.
15. 3
16. Attention `y = x` ne copie pas l'objet, `y = x.copy()` le fait.
17. -15
18. `[4, 16]`
19. Poetry: gestion de dépendances et d'environnements virtuels (uv)
20. `**kwargs` est un dictionnaire d'arguments nommés.

## Regex

### Exemple pneus

https://regex101.com/r/Y9euEt/1

### Groupes

- `[a-z]` groupes: capture n'importe quelle lettre de a - z
- `[a-zA-Z]` groupes: capture n'importe quelle lettre de a - z ou A - Z
- `[a-zA-Z0-9]` groupes: capture n'importe quelle lettre de a - z ou A - Z ou 0 - 9
- `[^a-z]` groupes: capture n'importe quel caractère sauf a - z
- `[A-Z-]` groupes: capture n'importe quelle lettre de A - Z ou -

### Quantificateurs

- `*` zéro ou plusieurs `{0,}`
- `+` un ou plusieurs `{1,}`
- `?` zéro ou un `{0,1}`
- `{n}` exactement n
- `{n,}` au moins n
- `{n,m}` entre n et m

### Capture

- `()` capture
- `(?:)` non capturant

### Logique

- `|` ou

- Marquage de pneu
- Dates US par dates ISO
- Titres Markdown dans une page et les numéroter hiérarchiquement

### Exercice

- S'exercer à décoder un code de pneu dans regex101
- Implémenter cette regex en Python pour décoder un code de pneu
- La fonction retourne un dictionnaire avec les différents éléments
- P.ex. `{'marque': 'Michelin', 'largeur': 205, 'hauteur': 55, 'diametre': 16, 'indice_charge': 91, 'indice_vitesse': 'V'}`
  
## Mini projets

| Code    | Description                                 | Cahier des charges           |
| ------- | ------------------------------------------- | ---------------------------- |
| Snake   | Modulaire, fonctionnalités cools + pygame   | [snake.md](snakito.md)       |
| Rag     | Retrieval-augmented generation sur flux RSS | [rag.md](rag.md)             |
| Sdr     | Software defined radio (RTL SDR, Hack RF)   | [sdr.md](sdr.md)             |
| Traffic | Gestion traffic routier, bouchons, etc.     | ?                            |
| Scraper | Chercher appartements subventionnés         | [flatscrap.md](flatscrap.md) |
| Chill   | Classement des jeux du Chillout             | [gamehub.md](gamehub.md)     |
| Network | Map réseau et topologie                     | [network.md](network.md)     |
| Tower   | Jeu de tower defense                        | [tower.md](tower.md)         |
