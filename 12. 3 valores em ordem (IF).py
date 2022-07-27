#Algoritmo, Tarefa 11. Compra de maçâs (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 16/07/2022

"""
Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais)
 e escrevê-los em ordem crescente.
"""

Valor1 = int(input("Digite o Valor numero 1: "))
Valor2 = int(input("Digite o Valor numero 2: "))
Valor3 = int(input("Digite o Valor numero 3: "))

list = [Valor1, Valor2, Valor3]

if Valor1 == Valor2 or Valor2 == Valor3:
    print("Valores iguaeis nao serao lidos... Digite um valor diferente ")
elif Valor1 and Valor2 and Valor3:
    print("Os Valores foram Ordenados em Crescente ")
    print(sorted(list))









