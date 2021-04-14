#leia sexo da pessoa e só aceite "M" ou "F", caso esteja errado peça p digitar novamente

gender = ''
while gender != "M" and gender != "F":
    gender = str(input("Digite o seu sexo [M/F]: ")).strip().upper()

    if gender == "M":
        print("Ok, você é do sexo masculino.")
    if gender == "F":
        print("Ok, você é do sexo feminino.")
    else:
        print("Comando inválido, digite novamente.")