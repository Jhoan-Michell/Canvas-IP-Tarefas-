#Algoritmo tarefa 03.  3. Idade de um nadador (IF)
#Dev: Jhoan Michell Guzman
#Data: 09/07/2022

"""
Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as regras a seguir.
Para idade inferior a 5, qual mensagem deveríamos mostrar?
"""

Idade = int(input("Digite a sua Idade: "))

if Idade < 5:
    print("A Categoria do Nadador e: Iniciante ")
elif Idade >= 5 and Idade <= 7:
    print("A Categoria do Nadador e: Infantil ")
elif Idade >= 8 and Idade <= 10:
    print("A Categoria do Nadador e: juvenil ")
elif Idade >= 11 and Idade <= 15:
    print("A Categoria do Nadador e: Adolecente ")
elif Idade >= 16 and Idade <= 30:
    print("A Categoria do Nadador e: Adulto ")
elif Idade > 30:
    print("A Categoria do Nadador e: Senior ")