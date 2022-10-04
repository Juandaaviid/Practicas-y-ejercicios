bandera=True
while bandera==True:
    print("Hola, sigo procesando")
    opcion=input("Desea continuar (S/N)?")
    if opcion=="N":
        bandera=False

'''
acumulador=0
limite=int(input("Introduzca el limite: "))
for contador in range(1,limite,1):
    print(f"El contador es {contador}")
    costoproducto=int(input("Introduzca el costo del producto: "))
    acumulador=acumulador+costoproducto
print(f"El valor total del inventario es {acumulador}")


#EJEMPLO PARA EL RETO 3
acumulador=0
limite=int(input("Introduzca el limite: "))
for contador in range(1,limite,1):
    #EL CODIGO DEL RETO 2
    costo=100
    acumulador=acumulador+costo
print(f"El valor total es {acumulador}")
'''
