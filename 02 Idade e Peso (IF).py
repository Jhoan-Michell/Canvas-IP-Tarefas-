#Algoritmo tarefa 01.  2. Idade e Peso (IF)
#Dev: Jhoan Michell Guzman
#Data: 09/07/2022
"""
Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.
"""
Idade = int(input("Digite a sua Idade: "))
Peso = float(input("Digite o seu Peso: "))

if Idade < 20 and Peso <= 60:
    print("Com um peso de:", Peso,"Kg voce encaixa no grupo de risco: 9 ")
elif Idade < 20 and Peso > 60 and Peso <= 90:
    print("Com um peso de:", Peso,"Kg voce encaixa no grupo de risco: 8 ")
elif Idade < 20 and Peso > 90:
    print("Com um peso de:", Peso,"Kg voce encaixa no grupo de risco: 7 ")
elif Idade >= 20 and Idade <= 50 and Peso <= 60:
    print("Com um peso de:", Peso, "Kg voce encaixa no grupo de risco: 6 ")
elif Idade >= 20 and Idade <= 50 and Peso > 60 and Peso <= 90:
    print("Com um peso de:", Peso, "Kg voce encaixa no grupo de risco: 5 ")
elif Idade >= 20 and Idade <= 50 and Peso > 90:
    print("Com um peso de:", Peso, "Kg voce encaixa no grupo de risco: 4 ")
elif Idade > 50 and Peso <= 60:
    print("Com um peso de:", Peso, "Kg voce encaixa no grupo de risco: 3 ")
elif Idade > 50 and Peso > 60 and Peso <= 90:
    print("Com um peso de:", Peso, "Kg voce encaixa no grupo de risco: 2 ")
elif Idade > 50 and Peso > 90:
    print("Com um peso de:", Peso, "Kg voce encaixa no grupo de risco: 1 ")
