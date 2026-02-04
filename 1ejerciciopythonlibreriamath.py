#Hacer los siguientes ejercicios de Python con usando la biblioteca math
import math
#1.     Pida un número no negativo y muestra su raíz cuadrada.
num_raiz=float(input("Introduce un número no negativo y muestra su raíz cuadrada: "))
if num_raiz >=0:
    print(f"La raiz cuadrada de {num_raiz} es: {math.sqrt(num_raiz)}")
else:
    print ("El numero no puede ser negativo")

#2.     Pide un número real y muestra su redondeo hacia abajo y hacia arriba.

numero_real=float(input("Introduce un numero real para redondear hacia abajo y arriba: "))
print(f"Redondeo del numero {numero_real} hacia arriba: {math.floor(numero_real)}")
print(f"Redondeo del numero {numero_real} hacia abajo: {math.ceil(numero_real)}")

#3.     Pide los catetos a y b y muestra la hipotenusa

cateto_a=float(input("Introduce el cateto A: "))
cateto_b=float(input("Introduce el cateto_B: "))

print(f"La hipotenusa es: {math.hypot(cateto_a,cateto_b)}")


#4.     Pide un ángulo en grados y muestra sin y cos.

grados=float(input("Intruduce un alguno en grados"))
radianes=math.radians(grados)
print(f"El seno es: {math.sin(radianes)}")
print(f"El coseno es: {math.cos(radianes)}")

#5.     Pide un entero no negativo y muestra su factorial.

numero_factorial=int(input("Introduce un numero enterno no negativo"))

if (numero_factorial > 0):

    print(f"La factorial de{numero_factorial} es: {math.factorial(numero_factorial)}")
else:
    print("El numero debe ser NO NEGATIVO")


#6.     Pide un número positivo y muestra ln(x) y log10(x).

numero_logaritmo=float(input("Introduce un numero positivo para calcular logaritmos"))
if (numero_logaritmo >0):
    print(f"El logatirmo de: {numero_logaritmo} es: {math.log(numero_logaritmo)}")
    print(f"El logaritmo de 10 de: {numero_logaritmo} es: {math.log10(numero_logaritmo)}")
else:
    print("El numero debe ser mayor que cero")


#7.     Pide base y exponente y muestra base^exponente

base=float(input("Introduce una base: "))
exponente=float(input("Introduce un exponente: "))
print(f"Mostramos el resultado: {math.pow(base,exponente)}")


#8.     Pide dos números reales y una tolerancia relativa, y decide si son iguales (o casi).

valor1=float(input("Introduce el primer valor real: "))
valor2=float(input("Introduce el segundo valor real: "))
tol=float(input("Introduce la tolerancia relativa (ej. 0.05 para 5%): "))
son_cercanos = math.isclose(valor1, valor2, rel_tol=tol)
print(f"¿Son iguales (o casi)? {son_cercanos}")


#9.       Pide dos enteros y muestra su máximo común divisor (gcd) y mínimo común múltiplo (lcm).

entero1 = int(input("Introduce el primer entero: "))
entero2 = int(input("Introduce el segundo entero: "))
print(f"Máximo Común Divisor: {math.gcd(entero1, entero2)}")
print(f"Mínimo Común Múltiplo: {math.lcm(entero1, entero2)}")

