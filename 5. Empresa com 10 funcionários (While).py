#Algoritmo tarefa 005), 5. Empresa com 10 funcionários (While)
#Dev: Jhoan Michell Guzman Corrales
#Data: 13/07/2022

laco1 = 1
laco2 = True
laco3 = True

while laco1 <= 10:
    #Quadro do Laco principal
    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = input("Digite o Codigo do Funcionario: ")
    HorasTrabalhadas = float(input("Digite o Numero de Horas Trabalhadas: "))

    #----------------------------- Condicionais da Categoria G e Nurno N

    while laco2:
        Categoria = input("Digite a Categoria: ")
        if Categoria == 'O' or Categoria == 'G':
            laco2 = False
        else:
            print("As Categorias Possiveis sao: 'O' ou 'G', Digite novamente...")
            continue
        break

    #----------------------------- Turno M ou V ou N

    while laco3:
        Turno = input("Digite O Turno: ")
        if Turno == 'M' or Turno == 'V' or Turno == 'N':
            laco3 = False
        else:
            print("Os Turnos Posssiveis sao: 'M' ou 'V' ou 'N', Digite novamente...")
            continue
        break

    #-------------------------------- Condicionais para tratar Categoria 'G' e Turno 'N'

    if Categoria == "G" and Turno == "N":
       ValorHora = SalarioMinimo * 0.18
       SalarioInicial = HorasTrabalhadas * ValorHora
       if SalarioInicial <= 300:
           AuxilioAlimentacao = SalarioInicial * 0.20
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       elif SalarioInicial > 300 and SalarioInicial <= 600:
           AuxilioAlimentacao = SalarioInicial * 0.15
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       else:
           AuxilioAlimentacao = SalarioInicial * 0.05
           SalarioFinal = SalarioInicial + AuxilioAlimentacao


    #-------------------------------- Condicionais para tratar Categoria 'G' e Turno 'M' ou 'V'

    if Categoria == "G" and Turno == "M" or Turno == "V":
       ValorHora = SalarioMinimo * 0.15
       SalarioInicial + HorasTrabalhadas * ValorHora
       if SalarioInicial <= 300:
           AuxilioAlimentacao = SalarioInicial * 0.20
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       elif SalarioInicial > 300 and SalarioInicial <= 600:
           AuxilioAlimentacao = SalarioInicial * 0.15
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       else:
           AuxilioAlimentacao = SalarioInicial * 0.05
           SalarioFinal = SalarioInicial + AuxilioAlimentacao

    # -------------------------------- Condicionais para tratar Categoria 'O' e Turno 'N'

    if Categoria == "O" and Turno == "N":
       ValorHora = SalarioMinimo * 0.13
       SalarioInicial = HorasTrabalhadas * ValorHora
       if SalarioInicial <= 300:
           AuxilioAlimentacao = SalarioInicial * 0.20
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       elif SalarioInicial > 300 and SalarioInicial <= 600:
           AuxilioAlimentacao = SalarioInicial * 0.15
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       else:
           AuxilioAlimentacao = SalarioInicial * 0.05
           SalarioFinal = SalarioInicial + AuxilioAlimentacao

    # -------------------------------- Condicionais para tratar Categoria 'O' e Turno 'M' ou 'V'

    if Categoria == "O" and Turno == "M" or Turno == "V":
       ValorHora = SalarioMinimo * 0.10
       SalarioInicial = HorasTrabalhadas * ValorHora
       if SalarioInicial <= 300:
           AuxilioAlimentacao = SalarioInicial * 0.20
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       elif SalarioInicial > 300 and SalarioInicial <= 600:
           AuxilioAlimentacao = SalarioInicial * 0.15
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
       else:
           AuxilioAlimentacao = SalarioInicial * 0.05
           SalarioFinal = SalarioInicial + AuxilioAlimentacao
    #----------------------------------- Quadro de Resumo
    print("Codigo:", Codigo,"Horas Trabalhadas:", HorasTrabalhadas, "Categoria:", Categoria,"Turno:", Turno)
    print("Valor da Hora:", ValorHora,"Salario Incial:", SalarioInicial, "Auxilio Alimentacao:", AuxilioAlimentacao,
          "Salario Final:", SalarioFinal)

    laco1 = laco1 + 1
    laco2 = True
    laco3 = True
print("Fim")

