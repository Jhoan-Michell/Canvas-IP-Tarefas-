#Algoritmo, Tarefa 13. Altura e sexo (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 17/07/2022

"""
Tendo como entrada a altura e o sexo (codificado da seguinte forma: 1: feminino 2: masculino)
de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:

para homens: (72.7 * Altura) – 58
para mulheres: (62.1 * Altura) – 44.7
"""
print("Escolha seu sexo: ")
print("1) Feminino")
print("2) Masculino")

Sexo = int(input(":"))
Altura = float(input("Digite sua Altura: "))

if Sexo == 1 and Altura:
    Feminino = (62.1 * Altura) - 44.7
    print("Seu Peso ideal e de:", Feminino)
elif Sexo == 2 and Altura:
    Masculino = (72.7 * Altura) - 58
    print("Seu Peso ideal e de:", Masculino)