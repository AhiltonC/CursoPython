cant=int(input("Ingrese la cantidad de alumnos: "))

lista_alum=[]
for i in range(cant):
    alumno={}
    nombre=input("Ingrese nombre del estudiante: ")
    alumno['nombre']=nombre
    alumno['notas']=[]

    for n in range(3):
        nota = float(input(f'Ingrese la nota {n+1} del alumno: '))
        alumno['notas'].append(nota)

    lista_alum.append(alumno)

print(lista_alum)

for estudiante in lista_alum:
    if (sum(estudiante['notas'])/3) >= 4:
        print(estudiante['nombre'], sum(estudiante['notas'])/3, "APROBADO")
    else:
        print(estudiante['nombre'], sum(estudiante['notas'])/3, "DESAPROBADO")
        


