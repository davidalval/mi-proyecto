# 8.4 Ejercicios

# 1. Imprimir los números del 1 al 10.
for i in range (1,11):
    print (i)
# 2. Recorrer una lista de nombres y mostrar cada uno.
nombre=["David","Pepe","Jose","Maria"]
for i in nombre:
    print (i)


# 3. Sumar los números del 1 al 100 usando for.
suma=0
for i in range(1,101):
    suma=suma+i
    print(f"{suma}")


# 4. Pedir números al usuario hasta que escriba 0 (usar while).

numero_usuario=int(input("Escribe un numero (0 para salir): "))

while numero_usuario != 0:
    numero_usuario=int(input("Escribe un numero (0 para salir): "))
print("Fin del bucle")


# 5. Mostrar solo los números impares del 1 al 20.

for i in range (1,21,2):

    print (i)

for numero in range(1,21):
    if numero%2==1:
         print (numero)
