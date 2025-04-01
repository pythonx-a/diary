# Semaine 7/16

- [ ] Pandas
- [ ] Mémoization
- [ ] ABC


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
