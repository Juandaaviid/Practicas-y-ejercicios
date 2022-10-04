listaproductos = ['arroz', 'café', 'harina', 'azúcar', 'sal']
listaproductos = list(('arroz', 'café', 'harina', 'azúcar', 'sal'))

'''
#SABER EL NUMERO DE ITEMS QUE TIENE LA LISTA
tamañolistaproductos=len(listaproductos)
#RECORRER LA LISTA
for itemactual in range(0,tamañolistaproductos):
    print(listaproductos[itemactual])
    if listaproductos[itemactual]=='azúcar':
        print("El exceso de azucar provoca problemas de salud")
    if listaproductos[itemactual]=='café':
        print("No tomes mucho café antes de dormir")    
'''
#DEFINIR LISTA
listanumeros = [1,2,3,4,5,6,7,8,9,10]
#print(listanumeros)
#DEFINIR LISTA DINAMICAMENTE
listanumeros = list(range(1,11))
#print(listanumeros)
#AGREGAR AL FINAL UN ELEMENTO
listanumeros.append(11)
#INSERTAR UN ELEMENTO EN CUALQUIER POSICION
listanumeros.insert(0,66)
#OTRA FORMA DE INSERTAR EN UN RANGO DE ITEMS
listanumeros[7:7]=[100]
#BORRAR UN ELEMENTO DE LA LISTA
listanumeros.remove(4)
#REMPLAZAR UN ELEMENTO DE LA LISTA
listanumeros[3]=44
#REEMPLAZAR POSICIONES DE LA LISTA
listanumeros[2:5]=[15,16,17]
#ORDENAR UNA LISTA
#listanumeros.sort() #ORDENAR ASCENDENTEMENTE
#listanumeros.sort(reverse=True) #ORDENAR DESCENDENTEMENTE

#RECORRER LA LISTA
tamañolistanumeros=len(listanumeros)
for itemactual in range(0,tamañolistanumeros):
    print(listanumeros[itemactual])

#INDEXACION DE ITEMS CON NUMEROS NEGATIVOS
print(listanumeros[-1]) #MUESTRA EL ULTIMO
print(listanumeros[-2]) #MUESTRA EL PENULTIMO
print(listanumeros[-3]) #MUESTRA EL ANTEPENULTIMO

