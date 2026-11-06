import random

#Se crea lista de alumnos
alumnos = [
"ALVARADO RAMIREZ BRYAN MANUEL",
"CANIZALES PALAFOX ALAN SAMUEL",
"CHACON VILLEGAS ULISES GAMALIEL",
"CORONA PACHECO BENJAMIN",
"DELGADO QUIÑONEZ DANIEL",
"FLORES MARCOS DANIEL",
"GARCIA MENDOZA CARLOS EDUAN",
"GONZALEZ SAUCEDO DIEGO IVAN",
"GUILLEN VAZQUEZ ANGEL DE JESUS",
"GUILLEN VAZQUEZ IRIS GUADALUPE",
"HIGUERA GONZALES BRANDON ELIAS",
"LARIOS RINCON FERNANDO ALEXIS",
"LEMUS MARTINEZ FERNANDO DE JESUS",
"LUCEMA ANGULO LUNA LIZETH",
"MARQUEZ LIZARRAGA RENE",
"MATA SALAZAR NELLY JHOANA",
"MENDOZA ROMAY JOSE RICARDO",
"MOLLINEDO GAMEZ EVER",
"MONDRAGON ESCOBAR ANGEL",
"MONZON DE LEON JOSE IGNACIO",
"NAVARRO AVILA CHRISTIAN GAEL",
"PASILLAS LIZARRAGA GERMAN",
"PEREZ MORALES DANIEL JEREMIAS",
"RANGEL PEREZ SAMUEL",
"RODRIGUEZ CONTRERAS ANGELA JOSELINE",
"RODRIGUEZ CONTRERAS JESHUA FERNANDO",
"RUEDA GIL JOSE IVAN",
"SANTOS MONTIEL MAGDIEL IVAN",
"SOTO RUBIO LUIS ALBERTO",
"VELAZQUEZ FLORES NIMSI JEHIELI"
] 
alumnos_Pasados = [] #Se crea una lista vacia donde se pasaran los datos seleccionados por la libreria random
op = ""

#alumnos_Pasados.append(alumno_Seleccionado) #Se agrega a la lista vacia el dato seleccionado
#print("Alumno seleccionado:", alumno_Seleccionado) #Se imprime el dato que fue selecionado
#alumnos.remove(alumno_Seleccionado) #Se elimina el dato seleccionado para que no se repita la siguiente vez
#print(alumnos_Pasados) #Se imprime la lista vacia actualizada para que se muestre los seleccionados
#print(alumnos) #Se imprimen los datos actualizados con los datos seleccionados removidos
while True: #Se crea un ciclo while true para mostrar las actualizaciones del random.choice  

    op = input("Seleccione una opcion.... \n"
    "1.- Imprimir Al alumno seleccionado... \n" \
    "2.- Imprimir Nueva lista actualizada.... \n"
    "3.- Lista de alumnos que NO fueron seleccioandos... \n"
    "4.- Ver la cantidad de alumnos en las listas... \n"
    "5.- Salir del programa.... \n")
    if op == "1":
        alumno_Seleccionado = random.choice(alumnos) #Se pone random.choice para que seleccione un elemento aleatorio de la lista en este caso "alumnos"
        print("Alumno seleccionado:", alumno_Seleccionado)
        alumnos_Pasados.append(alumno_Seleccionado)#Se agrega el alumno seleccionado a la lista vacia llamada alumnos_Pasados
        alumnos.remove(alumno_Seleccionado) #Remueve el alumno de la lista alumnos para que no se repita el alumno y salgan los demas datos

    elif op == "2":
        print("Lista de alumnos seleccionados ", alumnos_Pasados)

    elif op == "3":

        print("Lista de Alumnos NO seleccionados... ",alumnos)
    elif op == "4":
        print("Cantidad de alumnos NO seleccionados ",len(alumnos))
        print("Cantidad de alumnos SI seleccionados ",len(alumnos_Pasados))
    elif op == "5":
        print("Gracias por su tiempo!... \n" \
        "Pase buen dia!......")
        break
    else:
        print("Opcion Incorrecta Por favor Seleccione la opcion correcta entre 1-5....")





