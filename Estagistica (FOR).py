from site import venv
resulMedia = mediaAccidentes = mediaVehiculos = acciAnterior = acciSeguinte = accMenor = cidades =  0

city1 = str(input("Infome a 1º cidade da pesquiça:\n "))
city2 = str(input("Infome a 2º cidade da pesquiça:\n "))
city3 = str(input("Infome a 3º cidade da pesquiça:\n "))
city4 = str(input("Infome a 4º cidade da pesquiça:\n "))
city5 = str(input("Infome a 5º cidade da pesquiça:\n "))

city = [city1, city2, city3, city4, city5]

for cid in city:
    codigo = int(input(f"Informe o codido da cidade '{cid}':\n "))
    veiculosPaseo = int(input(f"Informe o numero de veiculos de paseo na ciudade '{cid}':\n"))
    nroAccidenteTransito = int(input(f"Informe o numero de Accidente de tramsito de '{cid}':\n"))

    mediaVehiculos += veiculosPaseo

    if veiculosPaseo < 2000:
        cidades += 1
        mediaAccidentes += nroAccidenteTransito

    if (cid == city1):
        acciAnterior = nroAccidenteTransito
    elif (cid == city2):
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior < acciSeguinte):
            acciMenor = acciAnterior
            cidade = city1
        else:
            acciMenor = acciSeguinte
            cidade = city2
    elif (cid == city3):
        acciAnterior = acciMenor
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior < acciSeguinte):
            acciMenor = acciAnterior
            cidade = cidade
        else:
            acciMenor = acciSeguinte
            cidade = cid
    elif (cid == city4):
        acciAnterior = acciMenor
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior < acciSeguinte):
            acciMenor = acciAnterior
            cidade = cidade
        else:
            acciMenor = acciSeguinte
            cidade = cid
    else:
        acciAnterior = acciMenor
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior < acciSeguinte):
            acciMenor = acciAnterior
            cidade = cidade
        else:
            acciMenor = acciSeguinte
            cidade = cid

    if (cid == city1):
        acciAnterior = nroAccidenteTransito
    elif (cid == city2):
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior > acciSeguinte):
            acciMaior = acciAnterior
            inCidade = city1
        else:
            acciMaior = acciSeguinte
            inCidade = city2
    elif (cid == city3):
        acciAnterior = acciMaior
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior > acciSeguinte):
            acciMaior = acciAnterior
            inCidade = inCidade
        else:
            acciMaior = acciSeguinte
            inCidade = cid
    elif (cid == city4):
        acciAnterior = acciMaior
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior > acciSeguinte):
            acciMaior = acciAnterior
            inCidade = inCidade
        else:
            acciMaior = acciSeguinte
            inCidade = cid
    else:
        acciAnterior = acciMaior
        acciSeguinte = nroAccidenteTransito
        if (acciAnterior > acciSeguinte):
            acciMaior = acciAnterior
            inCidade = inCidade
        else:
            acciMaior = acciSeguinte
            inCidade = cid

resultMedia = mediaVehiculos / 5
mediaAccidentes = mediaAccidentes / cidades
print("A media de Vehiculos de paseo na 5 ciudade e de: ", resultMedia)
print("A media de accidentes nas ciudade com menos de 2000 vehiculos de paseo é de: ", mediaAccidentes)
print("A cidade: ", cidade,"com um Indice menor de accidente é: ", acciMenor)
print("A cidade: ", inCidade,"com um Indice maior de accidente é: ", acciMaior)