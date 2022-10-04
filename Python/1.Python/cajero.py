from cajerofunciones import encabezado,validartarjeta,accesoerrado,error,validarclave,menu,consultarsaldo,retirar,consignar,despedida
from random import randint

tarjetas=['1052673675','1052425624','10267137809']
claves=['12345','67890','02567']
cuentas=['35003007123','05673789037','09036724613']
saldos=[0,0,0]

continuar=True
intentostarjeta=0
intentosclave=0

while intentostarjeta<3:
    
    tarjetausuario=validartarjeta(tarjetas)
    posicion=tarjetas.index(tarjetausuario)
    if tarjetausuario!="":
        
        intentostarjeta=3
        while intentosclave<3:
            if validarclave(claves)==True:
                intentosclave=3
                while continuar==True:
                    encabezado()
                    opcioncliente=menu()
                    if opcioncliente=="1":
                        consultarsaldo(saldos,posicion)
                    elif opcioncliente=="2":
                        saldo=retirar(saldos,posicion)     
                    elif opcioncliente=="3":
                        saldo=consignar(saldos,posicion)
                    elif opcioncliente=="4":
                        continuar=False
                    else:
                        error()
            else:
                intentosclave=intentosclave+1 
                accesoerrado(intentosclave)           
    else:
        intentostarjeta=intentostarjeta+1
        accesoerrado(intentostarjeta)    
despedida()