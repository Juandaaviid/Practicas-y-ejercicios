import tkinter as tk

class Aplicacion(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.crearControles()
    
    def crearControles(self):
        self.mondialLabel = tk.Label(self, text='Hola, Mundo!')
        self.mondialLabel.config(bg="#00ffff")
        self.mondialLabel.grid()
        self.quitButton = tk.Button(self, text='Salir', command=self.quit)
        self.quitButton.grid()

if __name__ == '__main__':
    app = Aplicacion()
    app.master.title('Demostración de Aplicación usando TKinter')
    app.mainloop()