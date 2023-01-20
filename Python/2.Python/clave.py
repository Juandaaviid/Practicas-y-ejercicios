import random
clave=[]
for i in range(10):
    numero=random.randint(1,9)
    clave.append(numero)
clave2=[]
clave1=[]
for i in range(len(clave)):
    if clave[i]//2 == 0:
        clave2.append(clave[i])
    else:
        clave1.append(clave[i])
clavecadena="".join([str(_) for _ in clave])
clave1cadena="".join([str(_) for _ in clave1])
clave2cadena="".join([str(_) for _ in clave2])
print(f"La clave maestra es :{clavecadena}")
print(f"La clave con pares es :{clave1cadena}")
print(f"La clave con impares es :{clave2cadena}")