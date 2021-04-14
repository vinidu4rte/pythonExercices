#PA com while mostrando os 10 primeiros termos e pergunte mais quantos termos quer ver

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
termos = 10
an = a1

print("Os 10 primeiros termos da PA são:",end=' ')
print(a1, end=' ')

while termos != 1:
    an = an + r
    termos -= 1
    print(an, end=' ')

print("\nMais quantos termos você quer ver?")
termos_2 = int(input("Digite a quantidade: "))

print("Os próximos termos da PA são:", end=' ')

while termos_2 != 0:
    an = an + r
    termos_2 -= 1
    print(an, end=' ')
