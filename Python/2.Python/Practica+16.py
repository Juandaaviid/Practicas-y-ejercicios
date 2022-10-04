#Clases y Objetos

class miprimeraclase:
    
    #atributos de instancia
    def __init__(self):
        print("hola")
    #metodos
    def mensaje(self):
        print("buenas tardes")
    def mensaje1(self):
       print("adios")

mensaje = miprimeraclase()
mensaje.mensaje()
mensaje.mensaje1()

class clase2:

    def __init__(self, numero):
        self.numero=numero
    def comparar(self):
        if self.numero > 0:
            print("el numero es porsitivo")
        elif self.numero < 0:
            print("el numero es negativo")
        elif self.numero == 0:
            print("el numero es cero")
    def ciclo(self):
        while self.numero <= 10:
            print(self.numero)
            self.numero += 1

ejemplo = clase2(0)
ejemplo.comparar()
ejemplo.ciclo()
#ejemplo = clase2(int(input("Dame un numero:")))
#ejemplo.ciclo()
