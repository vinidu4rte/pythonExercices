#leia varios números e só pare de ler quando o user digitar '999' e some os números digitados exceto o flag

soma = 0
n = 0
n1 = int(input("Digite um número, se quiser parar digite o número 999: "))
if n1 != 999:
    while n != 999:
        n = int(input("Digite mais um valor: "))
        soma += n

print("OK! O programa parou e a soma total dos valores digitados foi {}." .format(n1+soma-999))
