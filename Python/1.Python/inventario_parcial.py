from inventariofunciones import despedida, existencias, menutipomovimiento, menuproducto, procesos, menugestionproductos, agregarproductos, actualizarproductos, borrarproductos

listacodigos=[546,645,241,745,321]
listaproductos=['arroz','cafe','azucar','sal','harina']
listaprecios=[300,400,250,1000,600]

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
                agregarproductos(listacodigos,listaproductos,listaprecios)
            if opcionproductos==2:
                actualizarproductos(listacodigos,listaproductos,listaprecios)  
            if opcionproductos==3:
                borrarproductos(listacodigos,listaproductos,listaprecios)                          
            if opcionproductos==4:
                existencias(listacodigos,listaproductos,listaprecios)
                input("Presione cualquier tecla para continuar...")
    else:
        cantidad=int(input("Escriba la cantidad de productos: "))
        if cantidad>=0:

            producto=menuproducto()
            
            if producto=="6":
                despedida()
            else:
                
                if producto=="1":
                    arroz=procesos(movimiento,cantidad,arroz)
                if producto=="2":
                    cafe=procesos(movimiento,cantidad,cafe)                
                if producto=="3":
                    azucar=procesos(movimiento,cantidad,azucar)
                if producto=="4":
                    sal=procesos(movimiento,cantidad,sal)
                if producto=="5":
                    harina=procesos(movimiento,cantidad,harina)           
            
            existencias(arroz,cafe,azucar,sal,harina)
        else:
            print("El valor ingresado no es válido!")
