def sum(x):
    suma = 0
    for i in x:
        print(i)
        suma += i
    print("la suma es: ", suma)
    return suma
print("Ingrese menor")
menor = int(input())

print("Ingrese mayor")
mayor = int(input())

print(menor, mayor)

rango = range(menor, mayor)
print(rango)
sum(rango)
