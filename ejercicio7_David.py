#7.-  configura(**opciones) que acepte claves como color, tamaño y devuelva un dict con valores por defecto si faltan. Observa **


def configura(**opciones):

    configuracion_inicial={"color":"blanco",
                            "tamaño":"10",
                            "fuente":"Arial"
                        }

    configuracion_inicial.update(opciones)
    return configuracion_inicial

print (configura(color="verde",border=10))