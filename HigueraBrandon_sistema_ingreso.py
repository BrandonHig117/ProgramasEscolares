#Ejemplo avanzado de condicionales con ingenierias

print("Bienvenido al sistema de evaluación de ingenierías")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio académico: "))
print("CLAVES VALIDAS:\n 1. Ingeniería Civil \n 2. Ingeniería Mecánica\n 3. Ingeniería Eléctrica\n 4. Ingeniería en Sistemas")
op = input("Ingrese la clave de la ingeniería que desea evaluar: ")

if op == "1":
    print("Ha seleccionado Ingenieria Civil....")
    if(edad>=17 and promedio>=7.5):
        print("Felicidades, "+ nombre + " usted cumple con los requisitos para ingresar a la Ingeniería Civil., con un promedio de: "+str(promedio)+ "Bienvenido a Ingenieria Civil!")
    elif(edad>=17 and promedio<7.5):
        print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
        ", ya que su promedio es de "+str(promedio)+ " y el requisito mínimo es de 7.5 aunque cumple con la edad de: "+str(edad)+" años.\n Sigue esforzandote!")
    elif(edad<17 and promedio>=7.5):
        print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
        ", ya que su edad es "+str(edad)+ " años y el requisito mínimo es de 17 años aunque cumple con el promedio de: "+str(promedio)+" Felcidades!, Lo estaremos esperando!")
    else:
        print("Lo sentimos "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
        "ya que no cumple con la edad minima  y el promedio minimo que es de 7.5 y usted cuenta con: " +str(promedio))
elif op == "2":
    print("Ha seleccionado Ingenieria Mecánica....")
    if(edad>=17 and promedio>=8.0):
            print("Felicidades, "+ nombre + " usted cumple con los requisitos para ingresar a la Ingeniería Civil., con un promedio de: "+str(promedio)+ " Bienvenido a Ingenieria Mecanica!")
    elif(edad>=17 and promedio<8.0):
            print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            ", ya que su promedio es de "+str(promedio)+ " y el requisito mínimo es de 8.0 aunque cumple con la edad de: "+str(edad)+" años.\n Sigue esforzandote!")
    elif(edad<17 and promedio>=8.0):
            print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            ", ya que su edad es "+str(edad)+ " años y el requisito mínimo es de 17 años aunque cumple con el promedio de: "+str(promedio)+" Felcidades!, Lo estaremos esperando!")
    else:
            print("Lo sentimos "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            "ya que no cumple con la edad minima  y el promedio minimo que es de 8.0 y usted cuenta con: " +str(promedio))
elif op  == "3":
    print("Ha seleccionado Ingenieria Eléctrica....")
    if(edad>=17 and promedio>=8.5):
            print("Felicidades, "+ nombre + " usted cumple con los requisitos para ingresar a la Ingeniería Civil., con un promedio de: "+str(promedio)+ "Bienvenido a Ingenieria Electrica!")
    elif(edad>=17 and promedio<8.5):
            print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            ", ya que su promedio es de "+str(promedio)+ " y el requisito mínimo es de 8.5 aunque cumple con la edad de: "+str(edad)+" años.\n Sigue esforzandote!")        
    elif(edad<17 and promedio>=8.5):
            print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            ", ya que su edad es "+str(edad)+ " años y el requisito mínimo es de 17 años aunque cumple con el promedio de: "+str(promedio)+" Felcidades!, Lo estaremos esperando!")
    else:
            print("Lo sentimos "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            "ya que no cumple con la edad minima  y el promedio minimo que es de 8.5 y usted cuenta con: " +str(promedio))
elif op == "4":
    print("Ha seleccionado Ingenieria en Sistemas....")
    if(edad>=17 and promedio>=7.0):
            print("Felicidades, "+ nombre + " usted cumple con los requisitos para ingresar a la Ingeniería Civil., con un promedio de: "+str(promedio)+ "Bienvenido a Ingenieria en Sistemas!")
    elif(edad>=17 and promedio<7.0):
            print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            ", ya que su promedio es de "+str(promedio)+ " y el requisito mínimo es de 7.0 aunque cumple con la edad de: "+str(edad)+" años.\n Sigue esforzandote!")
    elif(edad<17 and promedio>=7.0):
            print("Lo sentimos, "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            ", ya que su edad es "+str(edad)+ " años y el requisito mínimo es de 17 años aunque cumple con el promedio de: "+str(promedio)+" Felcidades!, Lo estaremos esperando!")
    else:
            print("Lo sentimos "+ nombre + " usted no cumple con los requisitos para ingresar a la Ingeniería Civil.\n"
            "ya que no cumple con la edad minima  y el promedio minimo que es de 7.0 y usted cuenta con: " +str(promedio))
else:
    print("Clave inválida. Por favor, ingrese una clave válida del 1 al 4.")

