def menu():
    opcion = int(input(" ----\n|MENU|\n ---- \n 1. Agregar nuevo pasajero \n 2. Agregar ciudades a la lista de ciudades \n 3. Dado el DNI de un pasajero ver a que ciudad viaja \n 4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan para esa ciudad. \n 5. Dado el DNI de un pasajero, ver a que pais viaja \n 6. Dado un pais, ver cuantos pasajeros viajan a ese pais \n 7. salir del programa \n Eleccion: "))
    return opcion
def limpiarpantalla():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

pasajeros=[("Juan", 1098, "Giron"), ("Joan", 1099, "Roma"), ("Camila", 1010, "Berlin")] 
ciudades=[("Giron","Colombia"), ("Berlin", "Alemania"), ("Roma", "Italia")]
opcion = 0
while opcion!=7:
    opcion=menu()

    if opcion == 1:
        nombre=input("Ingrese el nombre del pasajero: ")
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        limpiarpantalla()
        print(" --------------------------------------------")
        print("|EL PASAJERO HA SIDO REGISTRADO EXITOSAMENTE!|")
        print(" --------------------------------------------")

    if opcion == 2:
        repetido=False
        while repetido == False:
            ciudad=str(input("ingrese ciudad: "))
            pais=str(input("ingrese pais: "))
            nuevaciudad=(ciudad,pais)
            if nuevaciudad in ciudades:
                print("la ciudad ya esta registrada, intente nuevamente")
            else:
                repetido=True
        ciudades.append(nuevaciudad)
        limpiarpantalla()
        print(" ------------------------")
        print("|CIUDAD AÑADIDA CON EXITO|")
        print(" ------------------------")

    if opcion == 3:
        buscardni=int(input("ingrese dni: "))
        for i in range(len(pasajeros)):
            if buscardni in pasajeros[i]:
                limpiarpantalla()
                print(" ----------------------------")
                print (f"|EL USUARIO VIAJARA A:  {pasajeros[i][2]}|")
                print(" ----------------------------")
                break
            else:
                limpiarpantalla()
                print("El usuario no aparece en el sistema")

    if opcion == 4:
        ciudadBuscar=str(input("Ingrese ciudad: "))
        contador=0
        for i in range(len(pasajeros)):
            if ciudadBuscar in pasajeros[i]:
                contador+=1
        limpiarpantalla()
        if contador>=1:
            print(" --------------------------")
            print (f"|{contador} Pasajeros viajan a {ciudadBuscar}|")
            print(" --------------------------")
        else:
            print(f"No hay pasajeros para {ciudadBuscar} aun")

    if opcion == 5:
        buscardni=int(input("Ingrese un dni: "))
        for i in range(len(pasajeros)):
            if buscardni in pasajeros[i]:
                ciudad=pasajeros[i][2]
        for i in range(len(ciudades)):
            if ciudad in ciudades[i]:
                limpiarpantalla()
                print(f"El usuario viaja a {ciudades[i][1]}")

    if opcion == 6:
        pais=str(input("ingrese un pais: "))
        for i in range(len(ciudades)):
            if pais in ciudades[i]:
                ciudad= ciudades[i][0]
                soloCiudades=[]
                while ciudad not in soloCiudades:
                    soloCiudades.append(ciudad)
            contadorpasajeros=0
            for i in range(len(soloCiudades)):
                for j in range(len(pasajeros)):
                    if soloCiudades[i] in pasajeros[j]:
                        contadorpasajeros+=1
            limpiarpantalla()
            print(f"{contadorpasajeros} Viajan con destino a {pais}")