#Algoritmo, Tarefa 6. Receber nomes e salários (While)
#Dev: Jhoan Michell Guzman Corrales
#Data: 19/09/2022

"""
Faça um programa que receba o salário de um funcionário chamado Carlos. Sabe-se que outro funcionário, João,
tem salário equivalente a um terço do salário de Carlos. Carlos aplicará seu salário integralmente na caderneta de poupança,
que rende 2% ao mês, e João aplicará seu salário integralmente no fundo de renda fixa, que rende 5% ao mês.
O programa deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou
ultrapasse o valor pertencente a Carlos.
"""

salarioCarlos = float(input("Digite o seu Salario: "))

salarioJoão = 1/3 * salarioCarlos
poupançaCarlos = salarioCarlos + (salarioCarlos * 0.02)
rendaFixaJoão = salarioJoão + (salarioJoão * 0.05)

mes = 1

while mes >0:
        if rendaFixaJoão >= poupançaCarlos:
            print("Mes:", mes,"A renda fixa de joão e de: ", round(rendaFixaJoão,2),"E a poupansa de Carlos e de: ",round(poupançaCarlos,2))
            break
        else:
            print("Mes:", mes, "A renda fixa de joão e de: ", round(rendaFixaJoão,2), "E a poupansa de Carlos e de: ",round(poupançaCarlos,2))
            poupançaCarlos = poupançaCarlos + (poupançaCarlos * 0.02)
            rendaFixaJoão = rendaFixaJoão + (rendaFixaJoão * 0.05)
            mes += 1
            continue