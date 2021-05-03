#leia sexo da pessoa e só aceite "M" ou "F", caso esteja errado peça p digitar novamente

gender = str(input("Digite o seu sexo [M/F]: ")).strip().upper()
while gender != "M" and gender != "F":   #só vai passar do while quando resolver problema.
    gender = str(input("Comando inválido. Digite o seu sexo [M/F]: ")).strip().upper()
print("Sexo {} registrado com sucesso!" .format(gender)) #isso só acontece quando sai do while
