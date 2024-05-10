import random

def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number :
        guess=int(input(f"ingrese un numero del 1 al {x}: "))
        if guess < random_number:
            print("Disculpe usted introdujo un numero muy bajo. ")
        elif guess > random_number:
            print("Disculpe usted introdujo un numero muy alto. ")

    print(f"Felicidades, Usted acerto con el numero correcto: {random_number}")

guess(60)