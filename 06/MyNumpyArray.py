"""
Créer une classe `MyNumpyArray` qui hérite d'une liste `list`.
Surcharger l'opérateur `+` et `*` pour que la liste se comporte comme dans Numpy.

```py
>>> a = MyNumpyArray([1,2,3])
>>> a + a
[2, 4, 6]
>>> a * 3
[3, 6, 9]
```"
"""
class MyNumpyArray(list):
    def __add__(self, other):
        return [a + b for a, b in zip(self, other)]
    
    def __mul__(self, other):
        return [a * b for a, b in zip(self, other)]
    
    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"
    
a = MyNumpyArray([1,2,3])
print(a + a)
print(a * 3)

