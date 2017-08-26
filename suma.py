class Dojo(object):
    """docstring for Dojo."""
    def __init__(self, min, max, s):
        self.menor = min
        self.mayor = max
        self.salto = s
        self.rango = range(menor, mayor, salto)

    def sum(self):
        suma = 0
        for i in self.rango:
            suma += i
        return suma

print("Ingrese menor")
menor = int(input())

print("Ingrese mayor")
mayor = int(input())


print("Ingrese salto")
salto = int(input())

calcular = Dojo(menor, mayor, salto)

suma = calcular.sum()
print("La suma es: ", suma)
