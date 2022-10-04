def limpiarpantalla():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def despedida():
    limpiarpantalla()
    print("---------------------------------------")
    print("|       ¡¡¡  HASTA PRONTO  !!!         |")
    print("---------------------------------------")

def menutipomovimiento():
    limpiarpantalla()
    print("---------------------------------------")
    print("| BIENVENIDO AL SISTEMA DE INVENTARIO |")
    print("---------------------------------------")
    print("*** Movimientos de inventario ***")
    print("E. ENTRADA")
    print("S. SALIDA")
    print("B. BAJA")
    print("P. GESTION DE PRODUCTOS >>")   
    print("X. SALIR")
    movimiento=input("Seleccione un movimiento de inventario: ")
    movimiento=movimiento.upper()
    return movimiento

def menugestionproductos():
    limpiarpantalla()
    print("---------------------------------------")
    print("|        GESTION DE PRODUCTOS          |")
    print("---------------------------------------")    
    print("1. Agregar un nuevo producto")
    print("2. Actualizar un producto")
    print("3. Borrar un producto")
    print("4. Listar productos")    
    print("5. << Regresar")     
    opcionmenugestion=int(input("Seleccione una opcion: "))
    return opcionmenugestion
    
def existencias(listacodigos, listaproductos,listaprecios):
    limpiarpantalla()
    print("---------------------------------------")
    print("|             EXISTENCIAS              |")
    print("---------------------------------------")
    for itemactual in range(len(listacodigos)):
        print(f"{listacodigos[itemactual]}. {listaproductos[itemactual]} : {listaprecios[itemactual]}")
    return True

def agregarproductos(listacodigos,listaproductos,listaprecios):
    existencias(listacodigos, listaproductos,listaprecios)
    continuar="S"
    while continuar=="S":
        existe=False
        codigonuevoproducto=int(input("Escriba el codigo del nuevo producto: "))
        nombrenuevoproducto=input("Escriba el nombre del nuevo producto: ")
        nombrenuevoproducto=nombrenuevoproducto.lower()    
        precionuevoproducto=int(input("Escriba el precio del nuevo producto: "))
        for itemactual in range(len(listacodigos)):
            if listacodigos[itemactual]==codigonuevoproducto:
                print("¡ ERROR El producto ya existe!")
                existe=True
        if existe==False:
            listacodigos.append(codigonuevoproducto)   
            listaproductos.append(nombrenuevoproducto)
            listaprecios.append(precionuevoproducto)
            ultimaposicion=len(listacodigos)-1
            print(f"{listacodigos[ultimaposicion]}. {listaproductos[ultimaposicion]} : {listaprecios[ultimaposicion]}")
            print("¡ El producto se agregó exitosamente !")        
        continuar=input("¿ Desea continuar agregando productos ? (S/N): ")
        continuar=continuar.upper()
    return listacodigos,listaproductos,listaprecios

def actualizarproductos(listacodigos,listaproductos,listaprecios):
    existencias(listacodigos, listaproductos,listaprecios)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto a actualizar: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            nombreproductoactualizar=input(f"Nombre actual: {listaproductos[itemactual]} - Escriba el nuevo nombre del producto: ")
            nombreproductoactualizar=nombreproductoactualizar.lower()    
            precioproductoactualizar=int(input(f"Precio actual: {listaprecios[itemactual]} Escriba el nuevo precio del producto: "))
            listaproductos[itemactual]=nombreproductoactualizar
            listaprecios[itemactual]=precioproductoactualizar
            print("¡ El producto se actualizó exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios

def borrarproductos(listacodigos,listaproductos,listaprecios):
    existencias(listacodigos, listaproductos,listaprecios)
    existe=False
    codigoproductoborrar=int(input("Escriba el codigo del producto a borrar: "))
    itemactual=0
    while itemactual<len(listacodigos):
        if listacodigos[itemactual]==codigoproductoborrar:
            existe=True
            confirmacion=input("¿Esta seguro de borrar el producto? (S/N): ")
            confirmacion=confirmacion.upper()
            if confirmacion=="S":
                #REMOVER ELEMENTO DE LA LISTA POR INDICE O POSICION
                listacodigos.pop(itemactual)
                listaproductos.pop(itemactual)
                listaprecios.pop(itemactual)
                #REMOVER POR VALOR
                #listacodigos.remove(listacodigos[itemactual])
                #listaproductos.remove(listaproductos[itemactual])
                #listaprecios.remove(listaprecios[itemactual])                 
                print("¡ El producto se borró exitosamente !")
        else:
            itemactual=itemactual+1
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios

def menuproducto():
    limpiarpantalla()
    print("*** Listado de productos ***")
    print("1. Arroz")
    print("2. Cafe")
    print("3. Azucar")
    print("4. Sal")
    print("5. Harina")
    producto=input("Seleccione un producto: ")
    return producto

def procesos(movimiento,cantidad,saldoproducto):
    if movimiento=="E":
        saldoproducto=saldoproducto+cantidad 
    if movimiento=="S" or movimiento=="B":
        if cantidad<=saldoproducto:
            saldoproducto=saldoproducto-cantidad
        else:
            print("No hay existencias suficientes de este producto")
    return saldoproducto