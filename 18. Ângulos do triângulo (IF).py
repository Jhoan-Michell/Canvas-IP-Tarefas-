#Algoritmo, Tarefa 18. Ângulos do triângulo (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 19/07/2022

"""
Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva
se o triângulo é Acutângulo, Retângulo ou Obtusângulo.
Sendo que:
Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º
"""

print("Digite o Valor do Primer Angulo: ")
Angulo1 = float(input(":"))
print("Digite o Valor do Segundo Angulo: ")
Angulo2 = float(input(":"))
print("Digite o Valor do ultimo Angulo: ")
Angulo3 = float(input(":"))

#----------- Triângulo Retângulo: possui um ângulo reto (igual a 90º) ------#

if Angulo1 == 90 or Angulo2 == 90 or Angulo3 == 90:
    print("E um Triângulo: Retângulo ")

 #---------- Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º) --------#

elif Angulo1 > 90 or Angulo2 > 90 or Angulo3 > 90:
      print("E um Triângulo: Obtusângulo ")

 #---------- Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º) -------#

elif Angulo1 < 90 and Angulo2 < 90 and Angulo3 < 90:
      print("E um Triângulo Acutângulo ")
