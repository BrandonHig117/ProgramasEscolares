# Ejemplo de tipos de datos
#Numericos
#Enteros numero cerrado por asi decirlo sin decimal 
numeroUsuario = 1711
edadUsuario = 25
#Flotantes expresan valores decimales
cambioUsuario = 23.2
promedio = 8.9
#Texto STR
nombre = "Brandon"
mensaje = "Bienvenido a la programación a x app por favor presione enter para continuar"
#Booleanos es un tipo solo puede tener verdadero o falso
esMayorDeEdad = True
esMenorDeEdad = False
#Estructuras
#Listas
listaNumerosPares = [2, 4, 6, 8, 10]
materias = ["Desarrollo software", "Arquitectura de computadoras", "Logica de Promgramación"]
#Tuplas a diferencia de las listas no se pueden modificar ya es un valor asignado
tuplaNumeros = (1, 2, 3, 4, 5)
tuplaMaterias = ("Desarrollo software", "Arquitectura de computadoras", "Logica de Promgramación")
#Rangos
rangoAlumnos = range(0, 4)
secuenciaFotos = range(0, 5)

print("Bienvenido a ejemplo de tipos de datos, presione la opcion del ejemplo que desea ver")
op = input("1.- Numericos\n2.- Texto\n3.- Booleanos\n4.- Listas\n5.- Tuplas\n6.- Rangos\n")

if op == "1":
    print("Ejemplo de Numericos Enteros...\n")
    print("Numero de usuario: ", numeroUsuario)
    print("Flotantes....\n")
    print("Edad del usuario: ", edadUsuario)
    print("Cambio del usuario: ", cambioUsuario)
    print("Promedio: ", promedio)
elif op == "2":
    print("Ejemplo de Texto STR...\n")
    print("Nombre del usuario: ", nombre)
    print("Mensaje: ", mensaje)
elif op == "3":
    print("Ejemplo de Booleanos...\n")
    print("Es mayor de edad: ", esMayorDeEdad)
    print("Es menor de edad: ", esMenorDeEdad)
elif op == "4":
    print("Ejemplo de Listas...\n")
    print("Lista de numeros pares: ", listaNumerosPares)
    print("Materias: ", materias)
elif op == "5":
    print("Ejemplo de Tuplas...\n")
    print("Tupla de numeros: ")
    for i in tuplaNumeros:
        print("Elemento de la tupla: ", i)
    print("Tupla de materias: ")
    for i in tuplaMaterias:
        print("Elemento de la tupla: ", i)
elif op == "6":
    print("Ejemplo de Rangos...\n")
    print("Rango de alumnos: ")
    for i in rangoAlumnos:
        print("Elemento del rango: ", i+1)# Se suma 1 para que el rango empiece en 1 y no en 0 y de el rango correcto
    print("Secuencia de fotos: ")
    for i in secuenciaFotos:
        print("Elemento de la secuencia: ", i) #Se pone sin el valor de 1 para demostrar como se ve sin sumar empezando desde el 0 llegando al numero 4
else:
    print("Opcion no valida")



