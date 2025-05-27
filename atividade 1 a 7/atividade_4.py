opcao=0
while (opcao!=5):
    print("-------Calculadora-------")
    print("1-soma")
    print("2-divisao")
    print("3-multiplicação")
    print("4-subtração")
    print("5-sair")
    opcao=int(input("Escolha uma opcao: "))
    if opcao==1:
        numero1=float(input("Escolha um numero:"))
        numero2=float(input("Escolha outro: "))
        resultado = numero1+numero2
        print(f"resultado: {numero1}+{numero2}={resultado}")
    elif opcao==2:
        numero1=float(input("Escolha um numero:"))
        numero2=float(input("Escolha outro: "))
        resultado = numero1/numero2
        print(f"resultado: {numero1}/{numero2}={resultado}")
    elif opcao==3:
        numero1=float(input("Escolha um numero:"))
        numero2=float(input("Escolha outro: "))
        resultado = numero1*numero2
        print(f"resultado: {numero1}x{numero2}={resultado}")
    elif opcao==4:
        numero1=float(input("Escolha um numero:"))
        numero2=float(input("Escolha outro: "))
        resultado = numero1-numero2
        print(f"resultado: {numero1}-{numero2}={resultado}")
    elif opcao==5:
        print("Voce fechou a calculadora")
        break