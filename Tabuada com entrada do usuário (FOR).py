#Algoritmo, Tarefa 2. Tabuada com entrada do usuário (FOR)
#Dev: Jhoan Michell Guzman Corrales
#Data: 01/08/2022

"""
Faça um programa para calcular a tabuada de qualquer número digitado pelo usuário.
"""

NrTabuada = int(input("Digite o Numero da Tabuada: "))

Multiplicador = 1

for Tabuada in range(10):
    print(NrTabuada, "x", Multiplicador, "=", NrTabuada * Multiplicador)
    Multiplicador +=1

