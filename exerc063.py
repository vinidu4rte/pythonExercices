#leia um número N e mostre os N próximos termos da sequência de Fibonacci

print("Escolha a quantidade de termos que quer ver da sequência de Fibonacci começando do 0.")
n = int(input("Sua escolha: "))
count = n
soma = n
print(0)
while count != 0:
    count -= 1
    soma += (n-1)
    print(soma, end=' ')

#sequencia: 0 1 1 2 3 5 8 13, ou seja, pega o número e soma pelo anterior.