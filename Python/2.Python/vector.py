from vector_func import principal, calculos
a,b=principal()
calculos(a,b)
magnitud,angulo_rad,angulo_gra=calculos(a,b)
print(f"La magnitud del vector es: {magnitud}")
print(f"el angulo del vector en radianes es: {angulo_rad} y en grados es: {angulo_gra}")
