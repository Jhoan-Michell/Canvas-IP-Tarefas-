#Algoritmo Tarefa 04. 4. Salário bruto (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 10/07/2022

"""
Faça um programa que receba o salário bruto de um funcionário e,
usando a tabela a seguir, calcule e mostre o valor a receber.
Sabe-se que este é composto pelo salário bruto acrescido de gratificação e descontado
o imposto de 7% sobre o salário.
"""

SalarioBruto = float(input("Digite seu Salario Bruto: "))
SalarioLiquido = float
imposto = 0.07

if SalarioBruto <= 350:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 100.00
    print("O Salario Liquido e de:", SalarioLiquido)
elif SalarioBruto > 350 and SalarioBruto <= 600:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 75.00
    print("O Salario Liquido e de:", SalarioLiquido)
elif SalarioBruto > 600 and SalarioBruto <= 900:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 50.00
    print("O Salario Liquido e de:", SalarioLiquido)
elif SalarioBruto > 900:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 25.00
    print("O Salario Liquido e de:", SalarioLiquido)
