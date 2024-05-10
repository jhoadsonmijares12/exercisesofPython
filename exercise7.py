import random

print ("Bienvenidos al Generador de contraseñas")

chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%#&*()^+.,?0123456789"

number = input ("Cantidad de contraseña a generar:")
number =int(number)

length = input("Ingrese el largo de su contraseña: ")
length= int (length)

print ("\n Aca esta su contraseña: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)    