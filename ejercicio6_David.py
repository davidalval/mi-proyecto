#6.-  solo_pares(*numeros) que devuelva una lista con los pares. Observa *. Utiliza listas


# SIN ASTERISCO LA FUNCION ESPERA UNA SOLA COSA
def pares(*numeros):
    pares_encontrados=[]

    for n in numeros:
        if n%2==0:
            #metemos en añadir(append) la "n"
            pares_encontrados.append(n)
#el return hay que sacarlo del bucle
    return pares_encontrados


print (pares(1,2,3,4,5,6,7,8,9,10))
