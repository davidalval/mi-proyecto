# 3.- factorial(n) para n >= 0. Recuerda 0!=1

n=int(input("Introduce un numero para calcular su factorial: "))


def factorial(n):
    if n < 0:
        return "Error: No existe el factorial de negativos"

    # Si es 0, devolvemos 1 directamente
    if n == 0:
        return 1


    multi=1

    for numero in range(1,n+1):

        multi=multi*numero

    return multi

print(f"La factorial del numero: {n} es: {factorial(n)}")

# 3.- (MOSTRANDO LAS MULTIPLICACIONES) factorial(n) para n >= 0. Recuerda 0!=1

n = int(input("Introduce un numero para calcular su factorial: "))

def factorial(n):


    if n < 0:
        return "Error: No existe el factorial de negativos"

    # Si es 0, devolvemos 1 directamente
    if n == 0:
        return 1

    multi = 1



    for numero in range(1, n + 1):
        anterior = multi  # Guardamos el valor viejo solo para mostrarlo en el print
        multi = multi * numero

        # ESTA ES LA LÍNEA MÁGICA: Imprime la operación actual
        print(f"Multiplico {numero} * {anterior} = {multi}")

    # IMPORTANTE: El return va pegado a la izquierda (fuera del bucle)
    # para que solo devuelva el resultado cuando termine TODAS las vueltas.
    return multi

# Llamamos a la función
resultado_final = factorial(n)
print(f"\nEl resultado final es: {resultado_final}")