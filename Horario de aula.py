contador = 1
voto = voto1 = voto2 = 0
while contador > 0:

    print("Escolha o seu horario: 1- 17/10/22 | 2- 18/10/22 | 3- 19/10/22")
    caso = input("Digite o numero que corresponde ao horario da sua preferencia: ")

    if caso == "1":
        horario = "17.10.22"
        print("O horario da sua preferencia e: ", horario)
        voto +=1
    elif caso == "2":
        horario = "18.10.2022"
        print("O horario da sua preferencia e: ", horario)
        voto1 += 1
    else:
        horario = "19.10.2022"
        print("O horario da sua preferencia e: ", horario)
        voto2 += 1

    print("O primer horario tem numero de votos: ", voto)
    print("O segundo horario tem numeros de votos: ", voto1)
    print("O terceiro horario tem numeros de votos: ", voto2)
    continue
