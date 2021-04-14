from random import randint
random = randint(0, 10)
choice = ''
attempts = 0

print("Estou pensando em um número entre 0 e 10, tente adivinhar!")
choice = int(input("Sua tentativa: "))
print(random)

if choice == random:
    print("Parabéns, você acertou de primeira!")

while choice != random:
    if choice != random:
        attempts += 1
        print("Você errou, tente novamente!")
        choice = int(input("Sua tentativa: "))

    if choice == random:
        attempts += 1
        print("Parabéns, você acertou após {} tentativas!" .format(attempts))

