#Algoritmo, Tarefa 3. Preço de produtos (FOR)
#Dev: Jhoan Michell Guzman Corrales
#Data: 01/08/2022

"""
Faça um programa que receba o preço, a categoria (1 – limpeza; 2 – alimentação; ou 3 – vestuário)
 e a situação (R – produtos que necessitam de refrigeração; e N – produtos que não necessitam de refrigeração).
 Calcule e mostre:
O valor do aumento, usando as regras que se seguem.
"""

Preco = PrecoComAumento = Imposto = NovoPreco = float
Categoria = int
Situacao = str
Imposto = 0.08

Preco = float(input("Digite o Preço do pruducto: "))
 #-------------------------------------- Categotia do producto ----------------------------

print("Digite a Categoria do Producto: ")
print("(1 - Limpeza) (2 - Alimentação) (3 - Vestuario)")
Categoria = int(input("Digite a Categoria do Producto: "))

 #-------------------------------------- Situacao do producto -----------------------------


if Preco <= 25 and Categoria == 1:
    PrecoComAumento = Preco * 1.05
    NovoPreco = PrecoComAumento * (1 - Imposto)
    if NovoPreco <= 50:
          print("Barato")
    elif NovoPreco > 50 and NovoPreco < 120:
          print("Normal")
else:
    print("Caro")

if Preco <= 25 and Categoria == 2:
 # -------------------------------------- Situacao do producto -----------------------------
    print("Situação: (R – produtos que necessitam de refrigeração); e (N – produtos que não necessitam de refrigeração).")
    Situacao = str
    Situacao = input("Digite Situaçao do Producto: ")
 # -----------------------------------------------------------------------------------------
if Preco <= 25 and Categoria == 2 or Situacao == "R":
    PrecoComAumento = Preco * 1.08
    NovoPreco = PrecoComAumento * (1 - 0.05)
    if Preco <= 25 and NovoPreco <= 50:
        print("Barato")
    elif NovoPreco > 50 and NovoPreco < 120:
        print("Normal")
    else:
        print("Caro")
else:
    PrecoComAumento = Preco * 1.10
    NovoPreco = PrecoComAumento * (1 - Imposto)
    if Preco <= 25 and NovoPreco <= 50:
        print("Barato")
    elif NovoPreco > 50 and NovoPreco < 120:
        print("Normal")
    else:
        print("Caro")

 #------------------------------------ Mayor que 25 ------------------------------

if Preco > 25 and Categoria == 1:
      PrecoComAumento = Preco * 1.12
      NovoPreco = PrecoComAumento * (1 - Imposto)
      if NovoPreco <= 50:
           print("Barato")
      elif NovoPreco > 50 and NovoPreco < 120:
           print("Normal")
      else:
           print("Caro")

if Preco < 25 and Categoria == 2 or Situacao == "R":
       PrecoComAumento = Preco * 1.15
       NovoPreco = PrecoComAumento * (1 - Imposto)
       if Preco > 25 and NovoPreco <= 50:
           print("Barato")
       elif NovoPreco > 50 and NovoPreco < 120:
           print("Normal")
       else:
           print("Caro")

else:
       PrecoComAumento = Preco * 1.18
       NovoPreco = PrecoComAumento * (1 - Imposto)
       if NovoPreco <= 50:
           print("Barato")
       elif NovoPreco > 50 and NovoPreco < 120:
           print("Normal")
       else:
           print("Caro")







