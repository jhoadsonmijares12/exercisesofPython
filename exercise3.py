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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(50)