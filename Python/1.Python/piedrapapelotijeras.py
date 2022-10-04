import random
seguir_jugando=True
puntos_maquina=0
puntos_humano=0
while seguir_jugando==True:
    numeroaleatorio=random.randint(1,3)
    if numeroaleatorio==1:
        seleccion_maquina="Piedra"
    elif numeroaleatorio==2:
        seleccion_maquina="Papel"
    else:
        seleccion_maquina="Tijeras"
    print("JUEGO PIEDRA, PAPEL O TIJERAS")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    opcion=input("Seleccione su opcion para jugar: ")
    if opcion=="1":
        seleccion_humano="Piedra"
    elif opcion=="2":
        seleccion_humano="Papel"
    elif opcion=="3":
        seleccion_humano="Tijeras"
    else:
        seguir_jugando=False
        break
    if seleccion_maquina==seleccion_humano:
        print(f"La maquina selecciono {seleccion_maquina} y usted {seleccion_humano}, es un empate!")
    else:
        if seleccion_maquina=="Piedra" and seleccion_humano=="Papel":
            ganador="el humano"
            puntos_humano=puntos_humano+1
        if seleccion_maquina=="Piedra" and seleccion_humano=="Tijeras":
            ganador="la maquina"
            puntos_maquina=puntos_maquina+1            
        if seleccion_maquina=="Papel" and seleccion_humano=="Tijeras":
            ganador="el humano"
            puntos_humano=puntos_humano+1           
        if seleccion_maquina=="Papel" and seleccion_humano=="Piedra":
            ganador="la maquina"
            puntos_maquina=puntos_maquina+1            
        if seleccion_maquina=="Tijeras" and seleccion_humano=="Piedra":
            ganador="el humano"   
            puntos_humano=puntos_humano+1               
        if seleccion_maquina=="Tijeras" and seleccion_humano=="Papel":
            ganador="la maquina"
            puntos_maquina=puntos_maquina+1            
        print(f"La maquina selecciono {seleccion_maquina} y usted {seleccion_humano}, el ganador es {ganador}")
print("FIN DEL JUEGO, GRACIAS POR JUGAR")
print(f"La maquina obtuvo {puntos_maquina} puntos")
print(f"Usted obtuvo {puntos_humano} puntos")
if puntos_maquina>puntos_humano:
   print("JAJAJAJAJA TE GANE!!!!")
elif puntos_maquina<puntos_humano:
   print("FELICITACIONES, LE GANASTE A LA MAQUINA, ERES UN GENIO!!!")
else:
   print("EMPATASTE CON LA MAQUINA!!!!")