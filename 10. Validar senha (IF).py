#Algoritmo Tarefa 10. Validar senha (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 16/07/2022

"""
Escreva um programa que verifique a validade de uma senha fornecida pelo usuário.
 A senha válida é o número 1234. Devem ser impressas as seguintes mensagens:
  ACESSO PERMITIDO caso a senha seja válida e  ACESSO NEGADO caso a senha
  seja inválida.
"""

Usuario = input("Digite seu Usuario: ")
Senha = input("Senha: ")


if Senha == "1234":
    print("ACESSO PERMITIDO ")
else:
    print("ACESSO NEGADO ")



