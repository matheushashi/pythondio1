#CRIANDO SISTEMA BANCARIO COM PYTHON DIO

menu = """
[d] deposito
[s] sacar
[e] extrato
[q] sair 
=>""" 

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do desposito:"))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:2f}\n"
        
        else:
            print ("Operacao falhou! Ovalor informado e invalido.")

    elif opcao =="s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operacao falhou! voce nao tem saldo suficiente.")
        
        elif excedeu_limite:
            print("operacao falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("operacao falhou! Numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print ("Operacao falhou! Ovalor informado e invalido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Nao foram realizadas as movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:2f}")

    elif opcao == "q":
        break

    else:
        print ("Operacao invalida, por favor selecione novamente a operacao desejada.")

    