# min_de_tres(a,b,c) sin usar min()
print("Intruducimos 3 numeros y comprobamos cual es el mas pequeño")
a=int(input("Introduce el primer numero: "))
b=int(input("Intruducimos el segundo numero: "))
c=int(input("Introducimos el tercer numero: "))


def min_de_tres(a,b,c):
    minimo=a

    if b < minimo:
        minimo=b

    if c < minimo:
        minimo=c

    return minimo

resultado=min_de_tres(a,b,c)
print (f"El numero mas pequeño de los 3 es: {resultado}");