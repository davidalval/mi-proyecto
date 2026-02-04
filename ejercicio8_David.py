#8.-  contar_vocales(texto) que devuelva un diccionario con conteos de a,e,i,o,u.
texto=input("Introduce un texto par analizar")

def analizar(texto):

    conteo={"a":0,"e":0,"i":0,"o":0,"u":0}

    texto_minusculas=texto.lower()

    for letra in texto_minusculas:

        if letra in "aeiou":
            conteo[letra]+=1


    return conteo

print (analizar(texto))
