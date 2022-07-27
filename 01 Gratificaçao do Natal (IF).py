#Algoritmo tarefa 01.     1. Gratificação de natal (IF)
#Dev: Jhoan Michell Guzman
#Data: 09/07/2022

"""
H = número de horas extras – (2/3 * ( número de horas falta )) * 60
"""

HorasExtras = float(input("Digite o Mumero de Horas Extras: "))
HorasFaltas = float(input("Digite o Mumero de Horas Faltas: "))

TotalMinutos = (HorasExtras - (2/3*HorasFaltas)) * 60

if TotalMinutos >= 2401:
    print("Total minutos:", TotalMinutos,"com Gratificaçao de Natal de: R$ 500,00 ")
elif TotalMinutos >= 1801 and TotalMinutos < 2401:
    print("Total minutos:", TotalMinutos,"com Gratificaçao de Natal de: R$ 400,00 ")
elif TotalMinutos >= 1201 and TotalMinutos < 1801:
    print("Total minutos:", TotalMinutos,"com Gratificaçao de Natal de: R$ 300,00 ")
elif TotalMinutos > 600 and TotalMinutos < 1201:
    print("Total minutos:", TotalMinutos,"com Gratificaçao de Natal de: R$ 200,00 ")
elif TotalMinutos < 600:
    print("Total minutos:", TotalMinutos,"com Gratificaçao de Natal de: R$ 100,00 ")

