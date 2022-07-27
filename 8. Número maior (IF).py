#Algoritmo Tarefa 08...  8. Número maior (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 16/07/2022

"""
Escreva um programa para ler 2 valores (considere que não serão informados valores iguais) e escrever o maior deles.
"""

N1 = float(input("Digite o valor numero 1: "))
N2 = float(input("Digite o valor numero 2: "))

if N1 > 0 and N2 < N1:
    print("O Valor numero 1:", N1," e Maior do que Valor numero dois... ")
elif N2 == N1 and N1 == N2:
    print("Valores iguaeis nao serao lidos... por favor digite um valor diferente... ")
else:
    print("O Valor numero 2:", N2," e Maior do que o primer Valor... ")



