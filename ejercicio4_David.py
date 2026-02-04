# 4.-  area_circulo(radio, pi=3.141592653589793) que devuelva el área

radio=int(input("Introduce el radio de la circunferencia pra calcular el área: "))

def area_circulo(radio,pi=3.141592653589793):

    area=pi*(radio**2)
    return area
#puedes no poner el valor de pi al imprimiral, ya esta arriba {area_circulo(radio)}
print (f"El area de la circunferencia es: {area_circulo(radio,pi=3.141592653589793)}")