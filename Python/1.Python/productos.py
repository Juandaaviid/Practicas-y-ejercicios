listaproductos=['arroz','cafe','azucar','sal','harina']

numeroitems=len(listaproductos)
for i in range(0,numeroitems,1):
    print(listaproductos[i])
    if listaproductos[i]=="azucar":
        print("<El exceso de azucar daña tu salud>")

for datos in listaproductos:
    print(datos)
