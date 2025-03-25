# Semaine 06/16

- [ ] Args et kwargs
- [ ] Héritage
- [ ] Construction de classes
- [ ] Decorateurs et mémoization
- [ ] Autoreload
- [ ] Une classe est une instance
- [ ] ABC



## Args et kwargs

`*args` et `**kwargs` sont utilisés pour passer un nombre variable d'arguments à une fonction.

## Construction de classes

### Une classe est une instance

```py
MaClasse = type(
    "MaClasse",
    (object,),
    {"x": 42, "hello": lambda self: print("Hello!")}
)
```

### `__new__`

`__new__` est une méthode spéciale qui est appelée avant `__init__`.
Elle est utilisée pour créer une nouvelle instance de la classe. C'est le vrai constructeur.

```py
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

## Héritage

### Exercice de surcharge

Créer une classe `MyNumpyArray` qui hérite d'une liste.
Surcharger l'opérateur `+` et `*` pour que la liste se comporte comme dans Numpy.

```py
>>> a = MyNumpyArray([1,2,3])
>>> a + a
[2, 4, 6]
>>> a * 3
[3, 6, 9]
```

## ABC

Une *Abstract Base Class* est une classe qui ne peut pas être instanciée.
Elle est utilisée pour définir une interface commune à plusieurs classes.

```py
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

Les collections sont très utiles :

```py
from collections.abc import MutableSequence

class MyList(MutableSequence):
    ...
```

### Protocol

```py
from typing import Protocol

class HasGetItem(Protocol):
    def __getitem__(self, index: int) -> object: ...

def func(obj: HasGetItem):
    print(obj[0])
```

## Décorateurs

Un décorateur est une fonction qui prend une fonction en argument et retourne une fonction.

```py
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def my_function():
    print("Hello!")
```

En Python un décorateur peut prendre des arguments :

```py
import functools

class MyDecorator:
    def __init__(self, *args, **kwargs):
        print("MyDecorator.__init__", args, kwargs)

    def __call__(self, func):
        print("MyDecorator.__call__ avec la fonction", func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Avant appel")
            result = func(*args, **kwargs)
            print("Après appel")
            return result

        return wrapper

@MyDecorator(42, hello="world")
def my_function():
    print("Hello!")

my_function()
```

`functolls.wraps` permet de copier les métadonnées de la fonction décorée.

Exemple de `property` :

```py
class MyProperty:
    """ Descriptor """
    def __init__(self, fget, fset=None):
        print("MyProperty.__init__", fget)
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Attribut en lecture seule")
        self.fset(instance, value)

    def setter(self, fset):
        return MyProperty(self.fget, fset)

class MyClass:
    def __init__(self, value):
        self._value = value

    @MyProperty
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        print(f"Set to {v}")
        self._value = v

obj = MyClass(23)
print(obj.value)     # 23
obj.value = 42       # Set valeur à 42
print(obj.value)     # 42
```

## Mémoization

La mémoization est une technique qui consiste à stocker les résultats d'une fonction pour éviter de les recalculer.

```py
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

En pratique on utilisera le décorateur `functools.lru_cache` :

```py
import functools

@functools.lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
