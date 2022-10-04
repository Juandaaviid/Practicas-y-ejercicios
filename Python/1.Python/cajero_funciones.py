#VARIABLES GLOBALES
saldo=1000000
usuario="1052673675"
clave="12345"
continuartransaccion=True
intentosfallidos=0
#FUNCION ENCABEZADO
def encabezado():
    print("-----------------------------------")
    print("| BIENVENIDO AL CAJERO AUTOMATICO |")
    print("-----------------------------------")
#FUNCION MENU
def menu():
    print("Seleccione una opcion:")
    print("(1) Consultar Saldo")
    print("(2) Retirar Dinero")       
    print("(3) Consignar")
    print("(4) Salir")
def despedida():
    print("-------------------------------------")
    print("| GRACIAS POR USAR NUESTROS SERVICIOS |")
    print("-------------------------------------")
#FUNCION VALIDAR CLAVE DE USUARIO
def validarclave(clave_ingresado):
    global intentosfallidos
    if clave_ingresado==clave:
        intentosfallidos=0
        print("Clave validada exitosamente")
        return True
    else:
        intentosfallidos=intentosfallidos+1
        print("Clave inválida")        
        return False
#FUNCION VALIDAR USUARIO
def validarusuario(usuario_ingresado):
    global intentosfallidos
    if usuario_ingresado==usuario:
        intentosfallidos=0
        print("Usuario validado exitosamente") 
        return True
    else:
        intentosfallidos=intentosfallidos+1
        print("Usuario inválido")  
        return False
#FUNCION CONSULTAR SALDO
def consultarsaldo(saldoactual):
    print(f"Su saldo actual es: {saldoactual}")
#FUNCION RETIRAR
def retirar(saldoactual):
    valorretiro=int(input("Escriba el valor a retirar:"))
    if valorretiro<=saldoactual:
        saldoactual=saldoactual-valorretiro
        print(f"Su nuevo saldo es: {saldoactual}")
    else:
        print("Fondos insufiencientes, Gracias por utilizar nuestros servicios!") 
    return saldoactual
#FUNCION CONSIGNAR
def consignar(saldoactual):
    valorconsignar=int(input("Escriba el valor a consignar:"))
    saldoactual=saldoactual+valorconsignar
    print(f"Su nuevo saldo es: {saldoactual}")    
    return saldoactual   
#CUERPO PRINCIPAL DEL PROGRAMA
while(continuartransaccion==True and intentosfallidos<3):
    encabezado()
    usuario_ingresado=input("Introduzca su usuario:")
    if validarusuario(usuario_ingresado)==True:
        clave_ingresado=input("Introduzca su clave:")
        if validarclave(clave_ingresado)==True:
            menu()
            opcion=input("Seleccione una opcion:")
            if opcion=="1":
                consultarsaldo(saldo)
            if opcion=="2":
                saldocliente=retirar(saldo)
            if opcion=="3":
                saldocliente=consignar(saldo)
            else:
                continuartransaccion=False
despedida()