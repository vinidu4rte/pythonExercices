#programa que lê dois valores e peça pro usuario escolher as opções do menu

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite mais um número inteiro: "))

print("""OK! Recebi os seus dois valores! Escolha no menu abaixo qual operação quer realizar:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa""")
choice = int(input("Escolha do menu: "))

while choice != 5:
    if choice == 1:
        print("A soma realizada resulta em {}." .format(n1+n2))
    if choice == 2:
        print("A multiplicação realizada resulta em {}." .format(n1*n2))
    if choice == 3:
        if n1 > n2:
            print("O primeiro valor digitado é maior.")
        if n2 > n1:
            print("O segundo valor digitado é maior.")
        else:
            print("Os dois valores são iguais.")
    if choice == 4:
        n1 = int(input("Digite um número inteiro: "))
        n2 = int(input("Digite mais um número inteiro: "))

    choice = int(input("Escolha do menu: "))

print("OK! Você saiu do programa.")