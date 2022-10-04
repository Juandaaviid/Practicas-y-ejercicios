inventario = {
    0:{'codigo':546,'nombre':'arroz', 'precio':3500, 'cantidad':0},
    1:{'codigo':645,'nombre':'cafe',  'precio':3500, 'cantidad':0},
    2:{'codigo':241,'nombre':'azucar','precio':4500, 'cantidad':0},
    3:{'codigo':745,'nombre':'sal',   'precio':1000, 'cantidad':0},
    4:{'codigo':321,'nombre':'harina','precio':600,  'cantidad':0}
}

tamañodiccionario=len(inventario)
print(f"El tamaño del inventario es de: {tamañodiccionario} productos")

def agregar(codigo,nombre,precio,cantidad):
    tamañodiccionario=len(inventario)
    inventario[tamañodiccionario] = {'codigo':codigo,'nombre':nombre,'precio':precio,'cantidad':cantidad}

def actualizar(indice,codigo,nombre,precio,cantidad):
    inventario[indice] = {'codigo':codigo,'nombre':nombre,'precio':precio,'cantidad':cantidad}

def listar():
    for item in inventario.items():
        print(item)

def borrar(indice):
    del(inventario[indice])

def eliminar():
    inventario.clear()

def buscar(clave):
    #inventario.get(clave)
    inventario.get(clave,"No existe esa clave en el diccionario")
    print(clave in inventario)

agregar(342,'aceite',1900,0)
agregar(351,'carne',12000,0)
actualizar(1,645,'café',4000,0)
borrar(5);
buscar('nombre')
listar()
eliminar()

#BUSQUEDA
print (inventario.get(1,"No hay un registro con ese indice"))

#BUSQUEDA DETALLADA
print (inventario[0].get("nombre","No hay un registro con ese nombre"))

#UBICAR ELEMENTOS DE UN DICCIONARIO
print(inventario[1]["nombre"])

#FUNCION ZIP
productos = zip(inventario[1].keys(), inventario[1].values()) 
print(type(productos))
productos = list(productos)
print(productos) 

#FUNCION ITEMS PARA EXTRAER CLAVES Y VALORES
for dato,valor in inventario[1].items():
    print (f"{dato} : {valor}")

#FUNCION KEYS PARA EXTRAER CLAVES
for clave in inventario[1].keys():
    print (f"{clave}")
    
#FUNCION VALUES PARA EXTRAER VALORES
for valor in inventario[1].values():
    print (f"{valor}")

inventario = {
    0:{'codigo':546,'nombre':'arroz', 'precio':3500, 'cantidad':0, 'presentacion':['bolsa']},
    1:{'codigo':645,'nombre':'cafe',  'precio':3500, 'cantidad':0, 'presentacion':['sobre','frasco','bolsa']},
    2:{'codigo':241,'nombre':'azucar','precio':4500, 'cantidad':0, 'presentacion':['sobre','bolsa']},
    3:{'codigo':745,'nombre':'sal',   'precio':1000, 'cantidad':0, 'presentacion':['bolsa','dispensador']},
    4:{'codigo':321,'nombre':'harina','precio':600,  'cantidad':0, 'presentacion':['bolsa','caja']}
}

for presentaciones in inventario[1]["presentacion"]:
    print (f"{presentaciones}")

