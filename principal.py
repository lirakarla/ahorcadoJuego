#autor: Karla Lira


import time
nombre=input("Como te llamas? ")
print("Bienvid@, "+nombre, "Es hora de jugar al ahorcado")
print(" ")

time.sleep(1)
print("comienza a adivinar")

time.sleep(0.5)
palabra='adivina'
tupalabra=''
vidas=5

while vidas>0:
    fallas=0
    for letra in palabra:
         if letra in tupalabra:
            print(letra, end="")
         else:
            print("*",end="")
            fallas+=1

    if fallas==0:
        print("\n------------------------------------------------------------------")
        print("                       Felicidades, ganaste                       ")
        print("------------------------------------------------------------------")

        break

    print(" ")
    tuletra=input("Introduce una letra: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("equivocacion")
        print(" ------------------------------------------------------------------")
        print("|                     Tu tienes,", +vidas, " vidas                 | ")
        print(" ------------------------------------------------------------------")

    if vidas==0:
        print("------------------------------------------------------------------")
        print("                             Lo siento, haz perdido!                            ")
        print("------------------------------------------------------------------")
else:
    print("gracias por participar")
