# Semaine 04/16

## Les classes sont des instances

Considérons une classe (plan de construction), d'un animal:

```py
class Animal:
    ... # Opérateur Ellipsis

animal = Animal()

type(animal) # Animal
type(Animal) # type
```

On constate que le type d'une classe est `type`, donc la classe `Animal` est déjà une instance.

Puisqu'il s'agit déjà d'une instance, cela me permet de rajouter un attribut à ma classe au *runtime*:

```py
Animal.toto = lambda self,x: 42
```

## Attributs

Par défaut, un attribut est en lecture/écriture. Donc je peux écraser le nom de mon animal.

```py
class Animal:
    def __init__(self, name):
        self.name = name

>>> animal = Animal("Foxy")
>>> animal.name
Foxy
>>> animal.name = "oops"
```

Une manière de faire c'est de cacher un attribut:

```py
class Animal:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name

>>> animal = Animal("Foxy")
>>> animal.get_name()
Foxy
>>> animal._name
Foxy
```

Oui mais on peut quand même écrire `animal._name = 'oops'` ? Absolument mais vous êtes un adulte responsable. Et donc, vous n'allez pas le faire.

### Getter

En programmation objet, on crée des *getter*, ce sont des méthodes qui retourne la valeur d'un attribut privé ou caché:

```py
class Animal:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    @property
    def name(self):
        return self._name
```

En Python on peut utiliser un *décorateur* qui se substitue à un attribut.

```py
>>> animal = Animal("Foxy")
>>> animal.name
Foxy
>>> animal.name = "oops"
AttributeError: Cannot change this attribute (read only)
```

Cela permet par exemple d'associer des actions à un attribut:

```py
class Animal:
    def __init__(self, name):
        self._name = name
        self._changes_left = 3
    def get_name(self):
        return self._name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        if self._changes_left > 0:
            self._name = new_name
            self._changes_left -= 1
        else:
            raise AttributeError("Cannot change name anymore")
```

```py
>>> animal = Animal("Foxy")
>>> animal.name = "Abc"
>>> animal._changes_left
2
>>> animal.name = "Abc"
>>> animal.name = "Abc"
>>> animal.name = "Abc"
AttributeError: Cannot change name anymore
```

### Getter ou attribut ?

La question se pose: est-ce préférable d'avoir `foo.name` ou `foo.name()` ?

Dans d'autres langage comme Java, il n'y a pas le choix, en Python une symbolique et donnée.

- Avec un attribut, le programmeur s'attend à ce qu'il n'y ait pas de calcul pour obtenir l'attribut
- Avec une méthode, le programmeur s'attend à ce qu'il puisse y avoir du calcul.

Considérons la classe `Vector`

```py
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def length(self):
        return math.sqrt(x**2 + y**2)

>>> v = Vector(5,8)
>>> v.length
```

Le calcul de `sqrt` peut prendre du temps, surtout sur une grande quantité de données. Un cas typique est le calcul de la longueur:

```py
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

>>> v = Vector(5,8)
>>> v.length # Précalculé ou pas ?
```

Parfois on s'autorise à avoir une méthode retournant la longueur au carré:

```py
    def length2(self):
        return self.x**2 + self.y**2
```

## Surcharge d'opérateurs

```py
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.length2())
    def length2(self):
        return self.x**2 + self.y**2
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        if hasattr(other, 'x') and hasattr(other, 'y'):
            return self.x * other + self.y * other

a = Vector(2,3)
b = Vector(5,6)
c = a + b
repr(c)
```

## Getitem et Getattr

Lorsque vous accédez à un attribut avec `.` comme dans `foo.x` vous dépendez de la méthode `getattr`, et quand vous accédez en utilisant les crochets, vous dépendez de `getitem`:

```py
class Foo:
    def __getattr__(self, letter):
        print(f"Getting attribute: {letter}")
        return ord(letter)
    def __getitem__(self, item):
        print(f"Getting item: {letter}")

>>> f = Foo()
>>> f.nimportequoi
>>> f['cequevousvoulez']
>>> f[42]
>>> f[1:4:5] # Slice
```

## Pint

Pint est pratique pour la conversion d'unités:

```py
import pint
ureg = pint.UnitRegistry()
u = 23 * ureg.meter
v = 42 * ureg.inch
w = u * v
w.to_base_units()

u = 23 * ureg.meter
v = 42 * ureg.second
w = u / v
w.to_base_units()

u = 23 * ureg.inch
v = 42 * ureg.hour
w = u / v
w.to_base_units()
w.to(ureg.km / ureg.hour)
w.to(ureg.km / ureg.ampere)
```

## Annotation de type

L'annotaton de type est utile pour le lexer et le linter mais pas à l'exécution:

```py
def length(v: Vector) -> float:
    return sqrt(v.x ** 2 + v.y ** 2)

def sum(array: list[Vector]) -> Vector:
    x = 0
    y = 0
    for v in array:
        x += v.x
        y += v.y
    return Vector(x, y)
```
