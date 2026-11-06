import random 

#alumnos que ya pasaron
#alumnos_pasados = []
profes = ["Mike"]
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
"VELAZQUEZ FLORES NIMSI JEHIELI",

] 

alumnosPasados = []
alumno_actual = random.choice(alumnos) #Seleccionar un alumno al azar
alumnosPasados.append(alumno_actual) #Agregara a la lista de alumnos que ya pasaron
#alumnos.pop(str(alumno_actual[0])) #Eliminar el alumno seleccionado de la lista de alumnos/ se puede usar remove o pop
#print(alumno_actual)
#alumnos.remove(alumno_actual) #Eliminara de la lista el alumno ya seleccionado
print(alumno_actual)
print(alumnosPasados)

#Al usar los alumnos que ya pasaronn agregarlos a otra lista y eliminarlo de la lista original para que no se repita