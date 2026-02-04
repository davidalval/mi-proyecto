# 1.-  es_par(n) que devuelva True si n es par, en otro caso False.

n=int(input("Introduce un numero para saber si es par: "))

def es_par(n):
    if  n%2==0:
        return True
    else:
        return False

if es_par(n):
    print(f"Es numero: {n}, es par")
else:
    print(f"El numero: {n}, es impar")