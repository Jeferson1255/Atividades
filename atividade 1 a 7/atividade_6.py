print("Conversor de C para F ou K")
print("1-Celsius para Fahrenheit")
print("2-Celsius para Kelvin")
opcao=int(input("Escolha uma opcao:"))
if opcao==1:
    c=float(input("\nEscreva a temperatura em Celsius:"))
    f=c*9/5+32
    print(f"Essa temperatura em Fahrnheit é:{f}F")
elif opcao==2:
    c=float(input("\nEscreva a temperatura em Celsius:"))
    k=c+273.15
    print(f"Essa temperatura em Kelvin é:{k}K")