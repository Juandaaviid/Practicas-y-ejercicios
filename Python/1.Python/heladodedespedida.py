from turtle import bgcolor
from turtle import *
from random import randint
from turtle import pencolor

bgcolor("black")
speed(0)

def limpiarpantlla():
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def despedida():
    print("***************************************")
    print("*    Nos vemos en el el 2o Modulo !!  *")
    print("***************************************")

def sabor(color1):
    if color1==1:
        r=randint(230,255)
        g=randint(0,100)
        b=randint(100,200)
        colormode(255)
        pencolor(r,g,b)
    elif color1==2:
        r=randint(0,100)
        g=randint(200,255)
        b=randint(0,200)
        colormode(255)
        pencolor(r,g,b)
    elif color1==3:
        r=randint(200,250)
        g=randint(150,200)
        b=randint(0,80)
        colormode(255)
        pencolor(r,g,b)

def plato(repet,size,rot):
    x=1
    while x<repet:
        pensize(1)
        r=randint(160,250)
        g=randint(110,255)
        b=randint(150,190)
        colormode(255)
        pencolor(r,g,b)
        fd(size+x*2)
        rt(rot)
        x+=1
    return plato
    input()

def chocolate(size):
    pensize(3)
    for i in range(size):
        r=randint(220,240)
        g=randint(100,185)
        b=randint(0,80)
        colormode(255)
        pencolor(r,g,b)
        circle(90-i,90)
        left(90)
        circle(90-i,90)
        left(18)

def helado(tam):
    pensize(6)
    for i in range(0,tam):
        sabor(color)
        circle(90-i,90)
        fd(-5)
        circle(90-i,90)
        right(18)

RED="\033[31m"

siono="S"
while siono!="N":
    print("*********************\nHELADOS DE DESPEDIADA \n*********************\n Qué quiere el tripulante ? :\n\t 1. Plato \n\t 2. Flor de  Chocolate \n\t 3. Bola de Helado")
    print(RED +"\t\33[31m 4. Helado completo  [2 BOLAS !!!]")
    print(RED +"\t\33[37m 5. Helado para todos \n\t 6. Salir \n\t")
    #figura=int(input("*********************\nHELADOS DE DESPEDIADA \n*********************\n Qué quiere el tripulante ? :\n\t 1. Plato \n\t 2. Flor de  Chocolate \n\t 3. Bola de Helado \n\t 4. Helado completo \n\t 5. Helado para todos \n\t 6. Salir \n\t"))
    figura=int(input("Seleccion :"))
    if figura==6:
        siono="N"
    elif figura==1:
        plato(80,200,90.911)
        siono=input("Quiere algo más : \n S/N: ")
        siono=siono.upper()
    elif figura==2:
        chocolate(90)
        siono=input("Quiere algo más : \n S/N: ")
        siono=siono.upper()
    elif figura==3:
        color=int(input("Que sabor quiere su helado?  :\n\t 1. Cereza\n\t 2. Limón\n\t 3. Durazno \n Seleccion : "))
        sabor(color)
        helado(90)
        siono=input("Quiere algo más : \n S/N: ")
        siono=siono.upper()
    elif figura==4:
        clear()
        for i in range(1):
            plato(50,200,90.911)
            right(50)
            penup()
            fd(210)
            pendown()
            color=int(input("Qué sabor quiere su helado?  :\n\t 1. Cereza\n\t 2. Limón\n\t 3. Durazno \n Seleccion : "))
            sabor(color)
            helado(80)
        for i in range(1):
            rt(120)
            penup()
            fd(100)
            pendown()
            color=int(input("Qué sabor quiere su helado?  :\n\t 1. Cereza\n\t 2. Limón\n\t 3. Durazno \n Seleccion : "))
            sabor(color)
            helado(75)
            chocolate(20)
            siono=input("Quiere algo más : \n S/N: ")
            siono=siono.upper()
    elif figura==5:
        clear()
        for i in range(3):
            plato(50,200,90.911)
            penup()
            fd(210)
            left(120)
            fd(-90)
            pendown()
            color=int(input("Qué sabor quiere su helado?  :\n\t 1. Cereza\n\t 2. Limón\n\t 3. Durazno \n Seleccion : "))
            sabor(color)
            helado(40)
            chocolate(20)
            penup()
            fd(380)
            left(130)
            pendown()
        siono=input("Quiere algo más : \n S/N: ")
        siono=siono.upper()
else:
    despedida()

