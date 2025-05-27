nome=input("Qual seu nome? ")
salario_fixo=float(input("Qual seu salario fixo? "))
vendas=float(input("Quantas vendas voce teve? "))
bonus=salario_fixo*0.15
salarioFinal=salario_fixo+bonus
if vendas>=20:
    print(f"Voce ganhou um bonus,seu salario é: {salarioFinal}")
else:
    print(f"Seu salario final é: {salario_fixo}")
