def prom_alto():
    cant=int(input("Ingrese la cantidad de alumnos: "))

    lista_alum=[]
    for i in range(cant):
        alumno={}
        nombre=input(f"Ingrese nombre del estudiante {i+1}: ")
        alumno['nombre']=nombre
        alumno['notas']=[]
        alumno['promedio']=[]

        for n in range(3):
            nota = float(input(f'Ingrese la nota {n+1} del alumno: '))
            alumno['notas'].append(nota)
            alumno['promedio'] =sum(alumno['notas'])/3
    
        lista_alum.append(alumno)

    ordenados = sorted(lista_alum, key=lambda alumno : alumno['promedio'])
    print(ordenados)

    print("El estudiante con promedio BAJO es :", ordenados[0])
    print("El estudiante con promedio ALTO es :", ordenados[-1])

prom_alto()