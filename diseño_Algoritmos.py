import qrcode

#Reto extra proporcionado por el profesor que es editar el QR Diseño, creando una clase llamada qr  donde controla tamaño, color y nivel llamando la clase QRCode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

print("Bienvenido al sistema de Creacion de QR!")
nombre = input("Por favor ingrese el nombre del codigo QR que va a generar: ")#Se agrega un input para que el usuario pueda elegir el nombre que guste dar

#Se crea condicion en caso de que usuario no llene el campo le mande mensaje que ocupa rellenar
if nombre != "":
    img = input("Por favor ingrese el texto o enlace que guste agregar en el codigo QR: ")#Igual se agrega input para decirle al usuario que genere el contenido del QR
    if img != "":
        qr.add_data(img)#Los datos del qr obteindos se pasa a la clase qr donde se podra moficar el diseño.

        #Reto extra hacer que el usuario eligar el color del QR
        colorFondo = input("Ingrese el color que quiere agregar al fondo del QR... En ingles por favor :")
        colorModulo = input("Ingrese el color que quiere agregar a los modulos oscuros... En ingles por favor :")

        contenidoi_qr = qr.make_image(fill_color=colorModulo, back_color=colorFondo)#Al pasar el qr hecho es donde pones los colores elegidos por el usuario. 
        contenidoi_qr.save(nombre+".png")#Se graba el codigo QR con el nombre que el usuario haya elegido
        print("QR Generado exitosamente "+nombre+".png")
    else:
        print("No puede crear un QR vacio")
else:
    print("No puede dejar el espacio vacio por favor ingrese los datoscorrectos del codigoQR..... \n Intente de nuevo!")