cant=int(input("Ingrese la cantidad de alumnos: "))

lista_alum=[]
for i in range(cant):
    alumno={}
    nombre=input("Ingrese nombre del estudiante: ")
    alumno['nombre']=nombre
    alumno['notas']=[]
    alumno['promedio']=[]

    for n in range(3):
        nota = float(input(f'Ingrese la nota {n+1} del alumno: '))
        alumno['notas'].append(nota)

        alumno['promedio'] = sum(alumno['notas'])/3

    lista_alum.append(alumno)

print(lista_alum)

c=0
while c <= cant:
    for n in cant:
        if alumno['promedio'][c] > alumno['promedio'][n]:
            print("El promedio mayor es: " )


for estudiante in lista_alum:
    print(estudiante['nombre'], "Su promedio es: ",sum(estudiante['notas'])/3)