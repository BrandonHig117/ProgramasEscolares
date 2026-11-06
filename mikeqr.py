import qrcode

nombre = input("Ingrese el nombre que quiere poner en el codigo QR: ")
img = qrcode.make(input("Ingrese el texto que quiere poner en el codigo QR: "))

img.save(nombre+".png")