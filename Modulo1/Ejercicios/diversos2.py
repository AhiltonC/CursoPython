#Ingreso de coeficientes
a=int(input("Coeficiente cuadrático: "))
b=int(input("Coeficinete lineal: "))
c=int(input("Termino independiente: "))

if a == 0:
    a=int(input("Escriba el Coeficiente cuadrático diferente de 0: "))

d=(b)**2-(4*a*c)

x1 = (-(b)+((d)**(1/2)))/(2*a)

x2 = (-(b)-((d)**(1/2)))/(2*a)

print(x1)
print(x2)

if d < 0:
    print("No tiene soluciones reales")

elif d > 0:
    print("Su primera solución es: ", x1)
    print("Su segunda solución es: ", x2)

else:
    print("Tiene solución única: ", x1)