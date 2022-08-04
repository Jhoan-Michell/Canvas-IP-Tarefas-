#Algoritmo, Tarefa 1. Estruturas condicionais e de repetição: Aumento salarial (FOR)
#Dev: Jhoan Michell Guzman Corrales
#Data: 31/07/2022

"""
Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:
a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;
b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;
c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017. Apresente todos os valores.
"""

SalarioInicial = PorcentualSalarial = ReajusteSalarial = SalarioAcumulado = 0
AnoInicial = 2000
AnoFinal = 2018


for i in range(AnoInicial, AnoFinal, 1):
    if i == 2000:
       SalarioInicial = 1000.00
       print(i, "SalarioInicial:", SalarioInicial, "%:", PorcentualSalarial, "Reajuste Salarial:", ReajusteSalarial, "Salario Acumulado:", SalarioAcumulado,)
    elif i == 2001:
         PorcentualSalarial = 0.00015
         ReajusteSalarial = SalarioInicial * PorcentualSalarial
         SalarioAcumulado = SalarioInicial + ReajusteSalarial
         print(i, "SalarioInicial:", SalarioInicial, "%:", round(PorcentualSalarial, 2), "Reajuste Salarial RS:", round(ReajusteSalarial, 2), "Salario Acumulado:", round(SalarioAcumulado, 2))
    else:
        print(i, "Salario Acumulado:", round(SalarioAcumulado, 2))
        ReajusteSalarial = SalarioAcumulado * PorcentualSalarial
        SalarioAcumulado = SalarioAcumulado + ReajusteSalarial
        print(i, "Salario Acumulado:", round(SalarioAcumulado, 2), "%:", round(PorcentualSalarial, 2), "Reajuste Salarial RS:", round(ReajusteSalarial, 2))
    PorcentualSalarial *= 2