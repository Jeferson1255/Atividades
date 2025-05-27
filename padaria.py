opcao=0
valor_total=0
frances=0
integral=0
doceLiso=0
doceFarofa=0
forma=0
valor_frances=0
valor_integral=0
valordoceLiso=0
valordoceFarofa=0
valorforma=0
while opcao!=6:
    print("------------PADARIA------------\n")
    print("1-Pão Frances\n")
    print("2-Pão Integral\n")
    print("3-Pão de Doce Liso\n")
    print("4-Pão de Doce Farofa\n")
    print("5-Pão de Forma\n")
    print("6-Finalizar compra.\n")
    print("-------------------\n")
    opcao=int(input("Escolha sua opção: "))
    if opcao==1:
        frances=int(input("Quantos pães frances voce quer:: "))
    elif opcao==2:
        integral=int(input("Quantos pães de integrais voce quer:  "))
    elif opcao==3:
        doceLiso=int(input("Quantos pães de doce voce quer:  "))
    elif opcao==4:
        doceFarofa=int(input("Quantos pães de farofa voce quer: "))
    elif opcao==5:
        forma=int(input("Quantos pães de forma voce quer:"))
    elif opcao==6:
        print("Voce saiu")
        frances !=0
        print ("Pão frances - quantidade: ", frances,"| Valor: R$" ,valor_frances)
        integral!=0
        print ("Pão integral - quantidade: ", integral,"| Valor: R$" ,valor_integral)
        doceLiso!=0
        print ("Pão doce liso - quantidade: ", doceLiso,"| Valor: R$" ,valordoceLiso)
        doceFarofa!=0
        print ("Pão doce farofa - quantidade: ", doceFarofa,"| Valor: R$" ,valordoceFarofa)
        forma!=0
        print ("Pão de forma - quantidade: ", forma,"| Valor: R$" ,valorforma)
        valorTotal=valordoceFarofa+valordoceLiso+valorforma+valor_frances+valor_integral
        print ("Valor o total: ",valorTotal)
    