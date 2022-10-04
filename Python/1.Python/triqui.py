def limpiarpantalla():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def actualizartablero(triqui):
    print("________________________________________________")
    print("                   T R I Q U I                  ")
    print("________________________________________________")
    for fila in triqui.keys():
        print(f"|\t{triqui[fila]['A']} \t|\t {triqui[fila]['B']} \t|\t {triqui[fila]['C']}\t|")
        print("________________________________________________")

triqui = {
        1:{"A":"","B":"","C":""},
        2:{"A":"","B":"","C":""},        
        3:{"A":"","B":"","C":""} 
}

contador=0
ganador1=False
ganador2=False
actualizartablero(triqui)

while ganador1!=True and ganador2!=True and contador<9:
    
    jugada1_fila=0
    while jugada1_fila<1 or jugada1_fila>3:
        jugada1_fila=int(input("JUGADOR 1: Escriba la fila (1,2,3): "))
        jugada1_columna=input("JUGADOR 1: Escriba la columna (A,B,C): ")
        jugada1_columna=jugada1_columna.upper()    
        while triqui[jugada1_fila][jugada1_columna]!="":
            print("LA POSICION ESTA OCUPADA !!!")
            jugada1_fila=int(input("JUGADOR 1: Escriba la fila (1,2,3): "))
            jugada1_columna=input("JUGADOR 1: Escriba la columna (A,B,C): ")
            jugada1_columna=jugada1_columna.upper()
    triqui[jugada1_fila][jugada1_columna]="X"

    limpiarpantalla()
    actualizartablero(triqui)

    if triqui[1]["A"]=="X" and triqui[2]["A"]=="X" and triqui[3]["A"]=="X":
        ganador1=True
        break
    if triqui[1]["B"]=="X" and triqui[2]["B"]=="X" and triqui[3]["B"]=="X":
        ganador1=True
        break
    if triqui[1]["C"]=="X" and triqui[2]["C"]=="X" and triqui[3]["C"]=="X":
        ganador1=True
        break
    if triqui[1]["A"]=="X" and triqui[1]["B"]=="X" and triqui[1]["C"]=="X":
        ganador1=True
        break
    if triqui[2]["A"]=="X" and triqui[2]["B"]=="X" and triqui[2]["C"]=="X":
        ganador1=True
        break
    if triqui[3]["A"]=="X" and triqui[3]["B"]=="X" and triqui[3]["C"]=="X":
        ganador1=True
        break
    if triqui[1]["A"]=="X" and triqui[2]["B"]=="X" and triqui[3]["C"]=="X":
        ganador1=True
        break
    if triqui[3]["A"]=="X" and triqui[2]["B"]=="X" and triqui[1]["C"]=="X":
        ganador1=True
        break

    jugada2_fila=0
    while jugada2_fila<1 or jugada2_fila>3:
        jugada2_fila=int(input("JUGADOR 2: Escriba la fila (1,2,3): "))
        jugada2_columna=input("JUGADOR 2: Escriba la columna (A,B,C): ")
        jugada2_columna=jugada2_columna.upper()    
        while triqui[jugada2_fila][jugada2_columna]!="":
            print("LA POSICION ESTA OCUPADA !!!")
            jugada2_fila=int(input("JUGADOR 2: Escriba la fila (1,2,3): "))
            jugada2_columna=input("JUGADOR 2: Escriba la columna (A,B,C): ")
            jugada2_columna=jugada2_columna.upper()
    triqui[jugada2_fila][jugada2_columna]="O"

    limpiarpantalla()
    actualizartablero(triqui)
    
    if triqui[1]["A"]=="O" and triqui[2]["A"]=="O" and triqui[3]["A"]=="O":
        ganador2=True
        break
    if triqui[1]["B"]=="O" and triqui[2]["B"]=="O" and triqui[3]["B"]=="O":
        ganador2=True
        break
    if triqui[1]["C"]=="O" and triqui[2]["C"]=="O" and triqui[3]["C"]=="O":
        ganador2=True
        break
    if triqui[1]["A"]=="O" and triqui[1]["B"]=="O" and triqui[1]["C"]=="O":
        ganador2=True
        break
    if triqui[2]["A"]=="O" and triqui[2]["B"]=="O" and triqui[2]["C"]=="O":
        ganador2=True
        break
    if triqui[3]["A"]=="O" and triqui[3]["B"]=="O" and triqui[3]["C"]=="O":
        ganador2=True
        break
    if triqui[1]["A"]=="O" and triqui[2]["B"]=="O" and triqui[3]["C"]=="O":
        ganador2=True
        break
    if triqui[3]["A"]=="O" and triqui[2]["B"]=="O" and triqui[1]["C"]=="O":
        ganador2=True
        break

    contador=contador+1

if ganador1 == True:
    print("JUGADOR 1 GANA !!!")
elif ganador2 == True:
    print("JUGADOR 2 GANA !!!")
else:
    print("ES UN EMPATE !!!")