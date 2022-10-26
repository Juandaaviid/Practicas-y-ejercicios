manzanas = int(input("Ingrese la cantidad de manzanas que desea: "))
valor_manzana=int(input("ingrese el precio por manzana: "))
total=manzanas*valor_manzana
if manzanas>=0 and manzanas<=3:
    total=total
elif manzanas>=4 and manzanas<=6:
    total-=(total*0.07)
elif manzanas>=7 and manzanas<=12:
    total-=(total*0.1)
elif manzanas >=13:
    total-=(total*0.15)
else:
    print(f"como va a comprar {manzanas} manzanas? ;-;")
    quit()
print(f"el total a pagar por {manzanas} manzanas con un precio por unidad de ${valor_manzana} es de: ${total}")