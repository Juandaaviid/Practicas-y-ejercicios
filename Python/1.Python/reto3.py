numeroPaquetes=int(input())
costoTotal=0
for n in range (numeroPaquetes):
    alto= float(input(""))
    ancho= float(input(""))
    profundo= float(input(""))
    volumen=(alto*ancho*profundo)
    costo=(volumen*5)
    if alto>30:
        costo=costo+2000
    else:
        costo=costo
    if costo>=10000:
        costo=costo*1.19
    else:
        costo=costo
    print(volumen)
    print(costo)
    costoTotal=costoTotal+costo
print(costoTotal)