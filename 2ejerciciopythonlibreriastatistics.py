#Hacer los siguientes ejercicios de Python con usando la biblioteca statistics
import statistics

#1.     Calcular el promedio/media de una lista de notas

notas = [6.5, 7.0, 5.5, 9.0, 7.0, 8.5, 6.0, 7.0, 4.5, 8.0]
print(f"Lista de notas: {notas}")

promedio = statistics.mean(notas)
print(f"Promedio: {promedio}")

#2.   Calcular la mediana de una lista de notas

mediana = statistics.median(notas)
print(f"Mediana: {mediana}")

#3.     Calcular la moda de una lista de notas

moda = statistics.mode(notas)
print(f"Moda: {moda}")

#4.     Calcular la desviación típica de una lista de notas

desviacion = statistics.stdev(notas)
print(f"Desviación típica: {desviacion:.4f}")

#5.     Calcular la varianza de una lista de notas

varianza = statistics.variance(notas)
print(f"Varianza: {varianza:.4f}")