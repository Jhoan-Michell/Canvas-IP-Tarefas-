#Algoritmo, Tarefa 11. Compra de maçâs (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 16/07/2022

"""
As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia,
 e R$ 0,25 se forem compradas pelo menos doze.
 Escreva um programa que leia o número de maçãs compradas, calcule e escreva
 o valor total da compra.
"""

NumMacas = int(input("Digite o numero de macas compradas: "))
NoDuzia = 0.30
Duzia = 0.25
TotalPreco = float

if NumMacas >= 12:
    TotalPreco = NumMacas *  Duzia
    print("Total Preco da compra de macas e de: R$", TotalPreco)
else:
    TotalPreco = NumMacas * NoDuzia
    print("Total Preco da compra de macas e de: R$", TotalPreco)