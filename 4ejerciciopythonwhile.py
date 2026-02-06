# 8.4 Ejercicios con WHILE

# 1. Imprimir los números del 1 al 10.
i=1;
while i<=10:

    print (i)
    i=i+1
# 2. Recorrer una lista de nombres y mostrar cada uno.
nombre=["David","Pepe","Jose","Maria"]
i=0;
while i<len(nombre):
    print (nombre[i])
    i=i+1

# 3. Sumar los números del 1 al 100 usando for.
suma = 0
i = 1
while i <= 100:
    suma += i
    i += 1
print(suma)  # si lo quieres solo al final

# (Si lo quieres como tú, imprimiendo la suma en cada paso:)
suma = 0
i = 1
while i <= 100:
    suma += i
    print(suma)
    i += 1
# 4. Pedir números al usuario hasta que escriba 0 (usar while).

numero_usuario = int(input("Escribe un número (0 para salir): "))
while numero_usuario != 0:
    numero_usuario = int(input("Escribe un número (0 para salir): "))
print("Fin del bucle")


# 5. Mostrar solo los números impares del 1 al 20.

i = 1
while i <= 20:
    if i % 2 == 1:
        print(i)
    i += 1

# (Alternativa más directa, saltando de 2 en 2)
i = 1
while i <= 20:
    print(i)
    i += 2