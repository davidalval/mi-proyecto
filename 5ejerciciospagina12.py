#6.1 REEMPLAZOS Y BUSQUEDAS
frase="Hola mundo mundo"

print(frase.replace("mundo","Python"))
print(frase.find("mundo"))
print(frase.count("mundo"))

#6.2 SLICING AVANZADO

texto="ABCDEFGHIJ"

print(texto[3:10:2])
print(texto[::-1])

#6.3.- Comprobaciones:

print("123".isdigit())
print("abc".isalpha())
print("123abc".isalnum())


#6.4.- Ejercicios prácticos adicionales

# 1) Pedir un texto y mostrarlo invertido.

texto=input("Introduce un texto: ")
print("texto invertido: ",texto[::-1])

# 2) contar cuantas veces aparece una palabra en una frase.

frase=input("Introduce una frase: ")
palabra=input("Intruduce la palabra: ")
print(f"La palabra {palabra} aparece {frase.count(palabra)} veces")

# 3) Validar que el usuario introduce un número positivo.

dato= input("Introduce un valor positivo: ")
if dato.isdigit() and int(dato) > 0:
    print ("Correcto")
else:
    print("Error no es un numero positivo")

