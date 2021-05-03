#peça um numero e mostre seu fatorial
import math

n = int(input("Digite um número inteiro e falarei o seu fatorial: "))

for f in range(n, 0, -1):
    if f != 1:
        print(f, end=' x ')
    elif f == 1:
        print(f, end=' = ')
print(math.factorial(n))

#usa-se o for para situações que se sabe os limites
#usa-se o while para situações que não se sabe ou sabe os limites