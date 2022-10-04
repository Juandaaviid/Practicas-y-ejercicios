def error():
    print("¡ERROR! Esa opcion no está disponible")   
def despedida():
    print("------------------------------------------")
    print("| GRACIAS POR UTILIZAR NUESTROS SERVICIOS |")
    print("------------------------------------------")
def encabezado():
    print("-----------------------------------")
    print("| BIENVENIDO AL CAJERO AUTOMATICO |")
    print("-----------------------------------")
def menu():
    print("Seleccione una opcion:")
    print("(1) Consultar Saldo")
    print("(2) Retirar Dinero")       
    print("(3) Consignar")
    print("(4) Salir")
    opcion=input("Seleccione una opcion:")
    return opcion
def menubasico():
    print("Seleccione una opcion:")
    print("(1) Consultar Saldo")
    print("(2) Consignar")
    print("(3) Salir")
    opcion=input("Seleccione una opcion:")
    return opcion
def accesoerrado(intentosfallidos):
    oportunidades=3-intentosfallidos
    print(f"Acceso errado, intentos restantes: {oportunidades}")
    if intentosfallidos==3:
        print("LADRON! LADRON! LADRON! LADRON! LADRON!")
def validartarjeta(tarjetas):
    tarjetausuario=input("Por favor introduzca su tarjeta: ")
    if tarjetausuario in tarjetas:
        return tarjetausuario
    else:
        return ""
def validarclave(claves):
    claveusuario=input("Por favor introduzca su clave: ")
    if claveusuario in claves:
        return True
    else:
        return False
def consultarsaldo(saldos,posicion):
    print(f"Su saldo actual es: {saldos[posicion]}")
def retirar(saldos,posicion):
    valorretiro=int(input("Escriba el valor a retirar:"))
    if valorretiro<=saldos[posicion]:
        saldos[posicion]=saldos[posicion]-valorretiro
        print(f"Su nuevo saldo es: {saldos[posicion]}")
    else:
        print("Fondos insufiencientes!")
    return saldos[posicion]    
def consignar(saldos,posicion):
    valorconsignar=int(input("Escriba el valor a consignar:"))
    saldos[posicion]=saldos[posicion]+valorconsignar
    print(f"Su nuevo saldo es: {saldos[posicion]}")
    return saldos[posicion] 