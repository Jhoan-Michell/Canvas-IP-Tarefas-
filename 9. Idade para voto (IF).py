#Algoritmo, tarefa 09... 9. Idade para voto (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 16/07/2022

"""
Escreva um programa para ler o ano de nascimento de uma pessoa e escrever
uma mensagem que diga se ela poderá ou não votar este ano
 (não é necessário considerar o mês em que ela nasceu).
"""

AnoNacimento = int(input("Digite o Ano do seu Nacimento: "))
AnoActual = 2022
Resposta = AnoActual - AnoNacimento

if Resposta >= 18:
    print("Com", Resposta,"Anos de idade voce podera votar. ")
else:
    print("Este ano voce nao podera votar, Voce nao atendiu a idade para votar ")

