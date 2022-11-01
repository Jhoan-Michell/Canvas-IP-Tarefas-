#Algoritmo, Tarefa 3. Preço de produtos
#Dev: Jhoan Michell Guzman Corrales
#Data: 01/08/2022

"""
Faça um programa que receba o preço, a categoria (1 – limpeza; 2 – alimentação; ou 3 – vestuário)
 e a situação (R – produtos que necessitam de refrigeração; e N – produtos que não necessitam de refrigeração).

"""
precoComAumento = novoPreco = 0
categoria = int
imposto = 0.08
situacao = str

preco = float(input("Digite o Preço do producto: "))
categoria = int(input("(1- Limpeza) (2 - Alimentação) (3 - Vestuario) \n Digite a Categoria do Producto:"))

if preco <= 25:
    if categoria == 1:
         precoComAumento = preco * 1.05
         novoPreco = precoComAumento * (1 - imposto)
    elif categoria == 2:
         situacao = str(input("(R – produtos que necessitam de refrigeração); e \n(N – produtos que não necessitam de refrigeração).\n Digite Situaçao do Producto: "))
    elif categoria == 2 and situacao == "R":
         precoComAumento = preco * 1.08
         novoPreco = precoComAumento * (1 - 0.05)
    elif categoria == 2 and situacao == "N":
         precoComAumento = preco * 1.10
         novoPreco = precoComAumento * (1 - 0.05)
    else:
         precoComAumento = preco * 1.10
         novoPreco = precoComAumento * (1 - imposto)

if preco > 25:
    if categoria == 1:
       precoComAumento = preco * 1.12
       novoPreco = precoComAumento * (1 - imposto)
    elif categoria == 2:
         situacao = str(input("(R – produtos que necessitam de refrigeração); e \n(N – produtos que não necessitam de refrigeração).\n Digite Situaçao do Producto: "))
    elif categoria == 2 and situacao == "R":
         precoComAumento = preco * 1.15
         novoPreco = precoComAumento * (1 - imposto)
    elif categoria == 2 and situacao == "N":
         precoComAumento = preco * 1.18
         novoPreco = precoComAumento * (1 - imposto)
    else:
         precoComAumento = preco * 1.18
         novoPreco = precoComAumento * (1 - imposto)

if novoPreco <= 50:
    print("Clasificação de producto: Barato.")
elif novoPreco >50 and novoPreco <= 120:
     print("Clasificação de producto: Normal.")
else:
     print("Clasificação de producto: Caro.")





