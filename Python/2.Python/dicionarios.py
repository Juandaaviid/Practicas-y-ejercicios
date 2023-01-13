notas={"Juan":[1.2, 3.1, 3.5]}

opcion=0
while opcion!=5:
    opcion=int(input("---MODULO DE NOTAS--- \n 1. Añadir un estudiante \n 2. Modificar una o mas notas \n 3. Crear e imprimir un diccionario de notas finales \n 4. Estudiantes que aprobaron y reprobaron, la maxima y minima nota y el promedio del curso \n 5. Salir \n Eleccion: "))
    if opcion == 1:
        print("---MODULO PARA AÑADIR ESTUDIANTES---")
        repetido = False
        while repetido == False:
            estudiante=input("Ingrese el nombre del estudiante: ")
            if estudiante in notas:
                print("Error: El estudiante ya se encuentra en el diccionario, intente nuevamente con otro nombre")
            elif estudiante not in notas:
                repetido=True
        notasnuevas=list(eval(input("Ingrese las notas del estudiante: ")))
        notas.update({estudiante: notasnuevas})
    
    elif opcion == 2:
        print("---MODULO PARA MODIFICAR NOTAS---")
        repetido = False
        while repetido == False:
            estudiante=input("Ingrese el nombre del estudiante: ")
            if estudiante not in notas:
                print("Error: El estudiante no se encuentra en el diccionario, intente nuevamente con otro nombre")
            elif estudiante in notas:
                repetido=True
        eleccion=int(input("¿Que nota desea modificar? 1, 2 o 3"))
        notas.update({estudiante: notasnuevas})

    elif opcion ==3:
        print("---MODULO NUEVO DICCIONARIO---")

