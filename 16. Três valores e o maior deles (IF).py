#Algoritmo, Tarefa 16. Três valores e o maior deles (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 17/07/2022

"""
Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
Considere que o usuário não informará valores iguais.
"""

Valor1 = int(input("Digite o primer valor: "))
Valor2 = int(input("Digite o segundo valor: "))
Valor3 = int(input("Digite o terceiro valor: "))

list = [Valor1, Valor2, Valor3]

if Valor1 and Valor2 and Valor3:
    print("O Valor Maior e: ")
    print(max(list))

