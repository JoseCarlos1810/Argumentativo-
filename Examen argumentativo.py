import math

def nivel_choque():
    #información necesario del nivel
    #formula utilizada: m1u1+m2u2=(m1+m2)v
    print("En esta prueba tendras que usar choque\nChocaste tu nave con un asteoride y se quedaron unidos")
    print("La nave tiene una masa de 8000kg y antes del choque llevaba 11195 m/s, la masa del asteroide es de 2000kg y estaba en reposo")
    print("Calcula la velocidad que llevaban el asteroide y la nave después del choque")
    print("Recuerda que la formula es m1u1+m2u2=(m1+m2)v")
    masa_nave=8000
    masa_asteroide=2000
    velocidad_inicial=11195
    velocidad_final=(masa_nave*velocidad_inicial)/(masa_nave+masa_asteroide)
    respuesta=float(input("Dime la velocidad que llevaran al final la nave y el asteroide: "))
    if math.isclose(respuesta, velocidad_final, rel_tol=0.1):
        print("Felicidades, es correcto\n")
        return True
    else:
        print("Esta mal\n")
        return False
def nivel_impulso():
    #información necesario del nivel
    #formula utilizada: I=m*Δv
    print("En esta prueba tendras que usar impulso\nLa nave y el asteroide se pararon y ahora quieres separarla del asteroide")
    print("La masa sigue siendo la misma y la velocidad necesaria para separarlos es de 2000 m/s")
    print("Recuerda que la fórmula del impulso es: I=m*Δv")
    velocidad_necesaria=2000
    masa=8000
    impulso=masa*velocidad_necesaria
    respuesta=float(input("Dime cuanto es el impulso con la velocidad necesaria para separar la nave: "))
    if math.isclose(respuesta, impulso, rel_tol=0.1):
        print("Felicidades, es correcto\n")
        return True
    else:
        print("Esta mal\n")
        return False
def main():
    print("Bienvenido, en este juego retaras tus conocimientos de física sobre impulso y choque")
    nombre = input("¿Cual es tu nombre? ")
    print("Buena suerte, esperemos que recuerdes física",nombre)
    #Revisión y ejecución de los desafíos 
    if nivel_choque() and nivel_impulso():
        print("Felicidades, has ganado, sientete orgulloso de tus conocimientos de física")
    else:
        print("Lamentablemente no lograste ganar el videojuegp")

main()




