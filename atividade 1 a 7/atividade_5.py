nome=input("Qual seu nome: ")
peso=float(input("Qual seu peso: "))
altura=float(input("Qual sua altura: "))
imc=peso/(altura*altura)
if imc<18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc<24.9:
    print("Peso normal")
else:
    print("Obesidade")