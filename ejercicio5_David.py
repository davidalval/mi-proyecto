#5.-   normaliza(texto) que quite espacios al inicio/fin y pase a minúsculas.


frase=input("Introduce la frase que quieres normalizar: ")

def texto(frase):

    mayusculas=frase.upper()
    espacios=mayusculas.strip()

    return espacios

print (f"{texto(frase)}")


#5.- SEGUNDA OPCION-normaliza(texto) que quite espacios al inicio/fin y pase a minúsculas.

frase=input("Introduce la frase que quieres normalizar: ")

def texto(frase):

    return frase.upper().strip()

print (f"{texto(frase)}")