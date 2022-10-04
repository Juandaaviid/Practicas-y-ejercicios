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
    print("I. INFORME EXISTENCIAS")
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
    
def existencias(inventario):
    limpiarpantalla()
    print("---------------------------------------")
    print("|             EXISTENCIAS              |")
    print("---------------------------------------")
    
    for clave in inventario.keys():
        print(f"{inventario[clave]['codigo']} . {inventario[clave]['nombre']} : {inventario[clave]['precio']} : {inventario[clave]['cantidad']} unidades")
    return True

def agregarproductos(inventario):
    existencias(inventario)
    continuar="S"
    while continuar=="S":
        existe=False
        codigonuevoproducto=int(input("Escriba el codigo del nuevo producto: "))
        nombrenuevoproducto=input("Escriba el nombre del nuevo producto: ")
        nombrenuevoproducto=nombrenuevoproducto.lower()    
        precionuevoproducto=int(input("Escriba el precio del nuevo producto: "))
        
        for clave in inventario.keys():
            if inventario[clave]['codigo']==codigonuevoproducto:
                print("¡ ERROR El producto ya existe!")
                existe=True
        
        if existe==False:
            siguientecodigo=int(max(inventario)+1)
            inventario[siguientecodigo]={'codigo':codigonuevoproducto,'nombre':nombrenuevoproducto,'precio':precionuevoproducto,'cantidad':0}
            print(f"{inventario[siguientecodigo]['codigo']} . {inventario[siguientecodigo]['nombre']} : {inventario[siguientecodigo]['precio']}")
            print("¡ El producto se agregó exitosamente !")        
        continuar=input("¿ Desea continuar agregando productos ? (S/N): ")
        continuar=continuar.upper()
    return inventario

def actualizarproductos(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto a actualizar: "))
    
    for clave in inventario.keys():
        if inventario[clave]['codigo']==codigoproductoactualizar:
            existe=True
            nombreproductoactualizar=input(f"Nombre actual: {inventario[clave]['nombre']} - Escriba el nuevo nombre del producto: ")
            nombreproductoactualizar=nombreproductoactualizar.lower()    
            precioproductoactualizar=int(input(f"Precio actual: {inventario[clave]['precio']} Escriba el nuevo precio del producto: "))
            inventario[clave]['nombre']=nombreproductoactualizar
            inventario[clave]['precio']=precioproductoactualizar
            print("¡ El producto se actualizó exitosamente !")
            break
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def borrarproductos(inventario):
    existencias(inventario)
    existe=False
    codigoproductoborrar=int(input("Escriba el codigo del producto a borrar: "))
    for clave in inventario.keys():
        if inventario[clave]['codigo']==codigoproductoborrar:
            existe=True
            confirmacion=input("¿Esta seguro de borrar el producto? (S/N): ")
            confirmacion=confirmacion.upper()
            if confirmacion=="S":   
                del(inventario[clave]['codigo'])
                print("¡ El producto se borró exitosamente !")
                break
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def entradas(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for clave in inventario.keys():
        if inventario[clave]['codigo']==codigoproductoactualizar:
            existe=True
            cantidadentrada=int(input(f"Cantidad actual: {inventario[clave]['cantidad']} - Escriba la cantidad de Entrada: "))
            inventario[clave]['cantidad']=inventario['clave']['cantidad']+cantidadentrada
            print("¡ El proceso se ejecuto exitosamente !")
            break
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return inventario

def salidas(inventario):
    existencias(inventario)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            cantidadsalida=int(input(f"Cantidad actual: {listacantidades[itemactual]} - Escriba la cantidad de Entrada: "))
            if cantidadsalida<=listacantidades[itemactual]:
                listacantidades[itemactual]=listacantidades[itemactual]-cantidadsalida
            else:
                print("¡ No hay suficientes existencias !")
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades

def bajas(listacodigos,listaproductos,listaprecios,listacantidades):
    existencias(listacodigos, listaproductos,listaprecios,listacantidades)
    existe=False
    codigoproductoactualizar=int(input("Escriba el codigo del producto: "))
    for itemactual in range(len(listacodigos)):
        if listacodigos[itemactual]==codigoproductoactualizar:
            existe=True
            cantidadbaja=int(input(f"Cantidad actual: {listacantidades[itemactual]} - Escriba la cantidad de Entrada: "))
            if cantidadbaja<=listacantidades[itemactual]:
                listacantidades[itemactual]=listacantidades[itemactual]-cantidadbaja
            else:
                print("¡ No hay suficientes existencias !")
            print("¡ El proceso se ejecuto exitosamente !")
    if existe==False:
        print("¡ ERROR El producto no existe!")
    return listacodigos,listaproductos,listaprecios,listacantidades