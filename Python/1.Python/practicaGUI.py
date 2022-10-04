from tkinter import * #Tk, Label, Button
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Una simple interfaz gráfica")
        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()
        self.botonSaludo = Button(master, text="Saludar", command=self.saludar)
        self.botonSaludo.pack()
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
    def saludar(self):
        print("Hola Tripulantes!")
root = Tk()                                 # Crear la ventana raíz (base) 
texto = Label(root, text="Hola Mundo!")     # Crear una etiqueta con texto
miVentana = VentanaEjemplo(root)            # Graficar la clase VentanaEjemplo
texto.pack()                                # Poner la etiqueta en la ventana
root.mainloop()                             # Iniciar el bucle de eventos