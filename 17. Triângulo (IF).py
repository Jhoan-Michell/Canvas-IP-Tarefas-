#Algoritmo, Tarefa 17. Triângulo (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 17/07/2022

"""
Escreva um programa que leia as medidas dos lados de um triângulo
e escreva se ele é Equilátero, Isósceles ou Escaleno.
Sendo que
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isóscele: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes.
"""

Medida1 = float(input("Digite a primer medida: "))
Medida2 = float(input("Digite a segunda medida: "))
Medida3 = float(input("Digite a terceira medida: "))



if Medida1 == Medida2 and Medida3 == Medida1:
     print("E um Triângulo: Equilátero ")
elif Medida1 == Medida2 or Medida3 == Medida2 or Medida1 == Medida3:
     print("E um Triângulo: Isóscele ")
elif Medida1 != Medida2 and Medida3 != Medida2 and Medida1 != Medida3:
     print("E um Triângulo: Escaleno ")

