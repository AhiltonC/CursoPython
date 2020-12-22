#Triángulo de MARIO

a=int(input("Ingrese la altura del triangulo de rango (1-8): "))

if a < 1 or a > 8:
    a=int(input("Ingrese un numero en el rango (1-8): "))
c = a
d = 0
while c >= 0 and d <= a:
    print(" "*c,"#"*d)
    c -= 1
    d += 1

