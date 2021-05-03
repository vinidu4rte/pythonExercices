from random import randint
random = randint(0, 10)
choice = ''
attempts = 0

print("Estou pensando em um número entre 0 e 10, tente adivinhar!")
choice = int(input("Sua tentativa: "))

if choice == random:
    print("Parabéns, você acertou de primeira!")

while choice != random:
    if choice != random:
        attempts += 1
        if choice > random:
            print("Hm... pensei em um número menor")
        if choice < random:
            print("Hm... pensei em um número maior")
        choice = int(input("Sua tentativa: "))


    if choice == random:
        attempts += 1
        print("Parabéns, você acertou após {} tentativas!" .format(attempts))