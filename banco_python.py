LIMITE_DE_SAQUES = 3

extrato = ''
limite = 500
numero_de_saques = 0
saldo = 0000

menu = '''
############################# BEM VINDO AO BANCO PYTHON!#############################

[0]Depositar
[1]Extrato
[2]Sacar
[3]Sair

############################# BEM VINDO AO BANCO PYTHON! #############################

'''

while True :
    opcao = input(menu)

    if opcao == '0' :
       print("\n#####Depositar#####")
       valor = float(input("Quanto gostaria de depositar : "))

       if valor > 0 :
           saldo += valor
           extrato += f"Deposito de R${valor :.2f}\n"
           
       else:
           print("Não é possivel realizar o deposito ")
    
    elif opcao == '1' :
        print("#####Extrato#####")
        print("Não foi realizada nenhuma movimentação " if not extrato else extrato)
        print(f"seu saldo é de : {saldo:.2f} ")

        print("##########################################################")

    elif opcao == '2' :
        print("\n#####Saque#####")
        valor = float(input("Quanto gostaria de sacar : "))
        if numero_de_saques == LIMITE_DE_SAQUES: break
        numero_de_saques += 1
        
        if saldo <= 0 : 
            print("Você não pode fazer essa opreção, pois está zerado!")
            break

        if valor > 500 :
            print("Você não pode tirar mais que R$500.00 por saque")
            break

        saldo -=  valor
        extrato += f"Saque : R${valor:.2f}"
        print("##########################################################")

    elif opcao == '3' :
        print("\n#####Fechando aplicativo#####")
        print("Obrigado por usar nosso banco ! ")
        print("##########################################################")
        break

    else :
        print("Operação Inválida, tente novamente")
