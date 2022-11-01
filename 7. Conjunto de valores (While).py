#Algoritmo, Tarefa 6. Receber nomes e salários (While)
#Dev: Jhoan Michell Guzman Corrales
#Data: 19/09/2022

"""
Faça um programa que leia um conjunto não determinado de valores e mostre o valor lido,
 seu quadrado, seu cubo e sua raiz quadrada.
Finalize a entrada de dados com um valor negativo ou zero.
"""

loop = True
import math

while loop:
    valor1 = float(input("Digite o valor: "))
    if valor1 <=0:
        print("Valor Invalido, valor menor que zero ou o mesmo nao seram aceitados.")
        break

    #-------------- Seu Quadrado ------------------#
    print("a raiz quadrada do valor 1:", valor1," e de: ", math.pow(valor1, 2))

    #--------------  Seu Cubo ---------------------#
    print("O cubo do valor 1:", valor1," e de: ", math.pow(valor1, 3))

    #-------------- Raiz quadrada ------------------#S
    print("a raiz quadrada do valor 1:", valor1," e de: ", math.sqrt(valor1))