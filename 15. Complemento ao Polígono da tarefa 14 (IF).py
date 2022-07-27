#Algoritmo, Tarefa 15. Complemento ao Polígono da tarefa 14 (IF)
#Dev: Jhoan Michell Guzman Corrales
#Data: 17/07/2022

"""
Acrescente as seguintes mensagens à solução da tarefa 14 conforme o caso.
Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO.
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

#-------------------------- NÃO É UM POLÍGONO.

if NrLados < 3:
   print("NÃO É UM POLÍGONO...")

#-------------------------- POLÍGONO NÃO IDENTIFICADO.

if NrLados > 5:
   print("POLÍGONO NÃO IDENTIFICADO...")