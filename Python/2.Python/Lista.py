import random
#Programa para añadir a filas y b columnas a una lista con numeros aleatorios decimales entre 0 y 1 o enteros entre 1 y 100
def enteros():
    lista=[]
    filas=int(input("ingrese el numero de filas para agregar: "))
    for i in range(filas):
        lista.append([])
    columnas=int(input("Ingrese el numero de columnas para agregar: "))
    for j in range(len(lista)):
        for x in range(columnas):
            numeros=random.randint(1,100)
            lista[j].append(numeros)
    print(lista)

def decimales():
    lista=[]
    filas=int(input("ingrese el numero de filas para agregar: "))
    for i in range(filas):
        lista.append([])
    columnas=int(input("Ingrese el numero de columnas para agregar: "))
    for j in range(len(lista)):
        for x in range(columnas):
            numeros=random.random()
            lista[j].append(numeros)
    print(lista)

eleccion=1
while eleccion == 1 or eleccion == 2 or eleccion ==3:
    eleccion=int(input("Desea utilizar: \n1. Enteros \n2.Decimales\n3. Salir\nEleccion: "))
    if eleccion == 1:
        enteros()
    elif eleccion == 2:
        decimales()
    elif eleccion == 3:
        print("Hasta la proximaaaa")
        break
    else:
        print("Entrada incorrecta, intente de nuevo")