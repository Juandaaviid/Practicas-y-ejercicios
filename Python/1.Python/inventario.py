from inventariofunciones import despedida, existencias, menutipomovimiento, entradas, salidas, bajas, menugestionproductos, agregarproductos, actualizarproductos, borrarproductos
inventario = {
    0:{'codigo':546,'nombre':'arroz', 'precio':3500, 'cantidad':0},
    1:{'codigo':645,'nombre':'cafe',  'precio':3500, 'cantidad':0},
    2:{'codigo':241,'nombre':'azucar','precio':4500, 'cantidad':2},
    3:{'codigo':745,'nombre':'sal',   'precio':1000, 'cantidad':0},
    4:{'codigo':321,'nombre':'harina','precio':600,  'cantidad':0}
}
movimiento=""
while movimiento!="X":
    movimiento=menutipomovimiento()
    if movimiento=="X":
        despedida()
    elif movimiento=="P":
        opcionproductos=0
        while opcionproductos<5:
            opcionproductos=menugestionproductos()
            if opcionproductos==1:
                agregarproductos(inventario)
            if opcionproductos==2:
                actualizarproductos(inventario)  
            if opcionproductos==3:
                borrarproductos(inventario)                          
            if opcionproductos==4:
                existencias(inventario)
                input("Presione cualquier tecla para continuar...")
    elif movimiento=="I":
            existencias(inventario)
            input("Presione cualquier tecla para continuar...")    
    elif movimiento=="E":
        entradas(inventario)
    elif movimiento=="S":
        salidas(inventario)  
    elif movimiento=="B":
        bajas(inventario)     
    else:
        despedida()