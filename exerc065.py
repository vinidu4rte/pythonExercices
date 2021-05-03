#leia quantos valores o usuario quiser (de opção de parar) e no final mostre a média, qual o maior digitado e qual o menor.

c = 0
soma = 0
n1 = 0
n2 = 0
n = int(input("Digite um número inteiro, se quiser parar o programa digite 0: "))
soma += n

while n != 0:
    c += 1
    n = int(input("Digite um número inteiro, se quiser parar o programa digite 0: "))
    soma += n
    if n != 0:
        n2 = n
        n1 = n
        if n > n1:   #se n for o maior, o maior é n e guarda. na próxima repetição, se o prox numero for maior que n1, guarda o número como o maior
            n1 = n
        if n < n2:
            n2 = n

print("A média entre os {} valores foi {}, sendo {} o maior valor digitado e {} o menor valor digitado." .format(c, (soma/c), n1, n2))
