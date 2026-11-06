#Cajero Automatico.
#PIN usando for 
#Menu de opciones con while
#validaciones con IF/ELIF/ELSE

print("Bienvenido a Brandon's Banco")

pin_Correcto = 12345
acceso = False # Usamoos variable booleana por si el usuario no ingresa el pin correcto no le de acceso
for i in range(3):  #Usamos un ciclo for para validar nip teniendo en range(3) que seria el numero de intentos 
    pin = int(input("ingresa tu nip : "))
    if pin == pin_Correcto:
        print("Bienvenido...")
        acceso = True
        break
    else:
        intentos_Restantes = 2 - i
        if intentos_Restantes > 0:
            print("Te quedan "+ str(intentos_Restantes) + " Intentos")
else:
    print("Excediste el numero de intentos.....intente mas tarde!.")

if acceso: #Se crea una condicion donde acceso si es = true pasa en caso de ser false no continuya
    saldo = 0
    while True: #Creamos un ciclo while que es un menu donde se repetira hasta que el usuario decida salir
        op = input("Bienvenido Elija la Opcion que desee utilizar.... \n" \
        "1.- Consultar Saldo.. \n" \
        "2.- Depositar.. \n" \
        "3.- Retirar.. \n" \
        "4.- Salir.. \n")

        if op == "1":
            print("Bienvenido a la Consulta de Saldo..... \n" \
            "Cuentas con un saldo de : " + str(saldo)+ " Pesos...")
        elif op =="2":
            print("Bienvenido a la zona de deposito..")
            deposito = int(input("Cuanto desea depositar?"))
            op1 = input("Es correcto?... Seleccione S(si) o N(no)")
            if op1 == "s":
                saldo = saldo + deposito
                print("Se ha depositado "+ str(deposito)+ " Cuentas con un saldo de " +str(saldo)+ " Pesos...")
            elif op1 == "n":
                print("Ingrese la cantidad corecta")
            else:
                print("error")
        elif op == "3":
            print("Bienvenido al Area de retiro")
            retiro = int(input("Cuanto desea retirar?"))
            op1 = input("Es correcto esta cantidad "+str(retiro)+"Seleccione S(si) o N(no)")
            if op1 == "s":
                if saldo < retiro:
                    print("No puedes retirar mas cantidad de la que tienes, cuentas con " +str(saldo)+ " Pesos")
                elif saldo >= retiro:
                    saldo = saldo - retiro
                    print("Listo... se retiro "+str(retiro)+" Cuentas con un saldo de :"+str(saldo)+" Pesos")
        elif op == "4":
            print("Adios....")
            break