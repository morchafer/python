# Valor cambiante de una variable de instancia:

class A:
    def __init__(self, v=1):
        self.v = v

    def set(self, v):
        self.v = v
        return v


a = A()
print(a.v)
print(a.set(a.v + 1))
print(a.v)

# ---------------------------------------------------------

# Valor cambiante de una variable de clase:


class A:
    X = 0

    def __init__(self, v=0):
        A.X += v


a = A()
b = A(1)
c = A(2)
print(c.X)

# ---------------------------------------------------------

# Una variable de clase puede tener el mismo nombre que su clase:


class A:
    A = 1


print(hasattr(A, 'A'))
print(A.A)

# ---------------------------------------------------------

# Argumento 'step' en una rodaja:


def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c


for x in I():
    print(x, end='')

# ---------------------------------------------------------

# Valor cambiante de una variable de instancia en función de dos objetos:


class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
print(a.v)
b = a
b.set()
print(a.v)
