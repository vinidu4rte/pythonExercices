#PA com while mostrando os 10 primeiros termos

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termos = 10
an = a1


print("Os 10 primeiros termos da PA são: {}" .format(a1))

while termos != 1:
    an = an + r
    termos -= 1
    print("Os 10 primeiros termos da PA são:",end=' ')
    print(an)
