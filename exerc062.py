#PA com while mostrando os 10 primeiros termos e pergunte mais quantos termos quer ver

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termos = 0
an = a1


print("Os 10 primeiros termos da PA são:", end=' ')
print(a1, end=' ')

while termos != 9:
    an = an + r
    termos += 1
    print(an, end=' ')


