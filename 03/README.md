# Semaine 03/16

- [x] REPL (Read Evaluate Parse Loop)
- [x] Paradigmes : oop, imperatif, procedural, fonctionnel, reflectif
- [x] 3.13
- [x] Scalaires, opérateurs

## Conteneurs

En Python il existe plusieurs conteneurs de données: 

- Les conteneurs séquentiels (p.ex. listes)
- Les conteneurs associatifs (p.ex. dictionnaires)

Python utilise les différentes types de parenthèses pour créer des conteneurs:

```py
u = [1,2,3] # Liste (tableau dynamique)
v = (1,2,3) # Tuple (tableau immuable)
w = {1,2,3} # Set (liste de clés en accès O(1))
x = {1:2, 3:4} # Dictionnaire (clé, valeurs)
```

Attention cependant, les conteneurs associatifs requièrent que les clés soient *hashable*, c'est à dire que l'on puisse exécuter : `hash(x)`. 

Les `listes` ne sont par exemple pas hashable. 

## Générateurs et Itérateurs

Lorsque vous utilisez `range(5000)` vous ne générez pas une liste de 5000 valeurs en mémoire. En réalité vous ne générez rien du tout. Ce n'est qu'à la demande que vous allez consommer les différents éléments.

```py
u = range(5) # Retourne un générateur
i = iter() # Demande un itérateur pointant sur le premier élément
next(i) # Retourne l'élément 0
next(i) # Retourne l'élément 1
...
# Jusqu'à l'erreur StopIteration
```

## Datamodel

Le *datamodel* de Python défini que toutes les actions de base du langage associées à des objets sont définies par des méthodes magiques qui démarrent par un `__` et se termine par un `__`. Par exemple : 

```py
u = [1,2,3]
u.__<tab> 
```

va vous donner la liste de toutes les méthodes magiques que l'objet `u` comprend. 

Python fonctionne selon le principe du *Duck Typing* qui veut dire: 

> Si ça a des pattes de canard, des ailes de canard
> et un bec de canard, c'est que c'est un canard.

Autrement dit, si un objet dispose des fonctionnalités propres à un canard, on considère cet objet comme un canard. Ainsi, si un objet dispose de la méthode `__iter__`, c'est que c'est un itérateur. 

Au diable donc l'héritage... (mais pas toujours)

## Modules

Une chose a retenir. Un dossier qui contient un `__init__.py` est un module et un module peut être importé depuis une console interactive ou un script: 

```py
import mymodule
```

Il suffit donc de déclarer vos fonctions et classes à l'intérieur de ce module pour en disposer depuis votre console interactive. 

Vous pouvez également créer un fichier `__main__.py` il sera utilisé comme point d'entrée dans votre projet si vous exécutez votre module comme un script: 

```bash
python -mmymodule
```
