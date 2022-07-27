#Algoritmo, Tarefa 14. Polígono (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 17/07/2022

"""
Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm).
Calcular e imprimir o seguinte:
Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
Se o número de lados for igual a 5 escrever PENTÁGONO.
Obs: O foco aqui é a lógica com o comando de controle IF, demais conhecimentos envolvidos pesquise mais.
"""

print("Os lados permitidos sao 3, 4, 5,")
NrLados = int(input("Digite o numero de lados: "))

 #-------------------------- TRIÂNGULO
if NrLados == 3:
   print("Digite o valor do Lado numero 1: ")
   Lado1 = float(input(""))
   print("Digite o valor de Lado numero 2: ")
   Lado2 = float(input(""))
   print("Digite o valor de Lado numero 3: ")
   Lado3 = float(input(""))

   ValorArea1 = (((Lado1 * Lado2) * Lado3) / NrLados)
   print("E um TRIÂNGULO, Com um valor de Area de:",ValorArea1)

#-------------------------- QUADRADO
if NrLados == 4:
   print("Digite o valor do Lado numero 1: ")
   Lado1 = float(input(""))
   print("Digite o valor de Lado numero 2: ")
   Lado2 = float(input(""))
   print("Digite o valor de Lado numero 3: ")
   Lado3 = float(input(""))
   print("Digite o valor de Lado numero 4: ")
   Lado4 = float(input(""))

   ValorArea2 = ((((Lado1 * Lado2) * Lado3) * Lado4) / NrLados)
   print("E um QUADRADO, Com um valor de Area de:",ValorArea2)

#-------------------------- PENTÁGONO
if NrLados == 5:
   print("Digite o valor do Lado numero 1: ")
   Lado1 = float(input(""))
   print("Digite o valor de Lado numero 2: ")
   Lado2 = float(input(""))
   print("Digite o valor de Lado numero 3: ")
   Lado3 = float(input(""))
   print("Digite o valor de Lado numero 4: ")
   Lado4 = float(input(""))
   print("Digite o valor de Lado numero 5: ")
   Lado5 = float(input(""))

   ValorArea3 = (((((Lado1 * Lado2) * Lado3) * Lado4) * Lado5) / NrLados)
   print("E um PENTÁGONO, Com um valor de Area de:",ValorArea3)

