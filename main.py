menu = """

Depoisitar dinheiro (D)
Sacar dinheiro (S)
Extrato bancario (E)
Sair do sistema (S)

=> """

saldoConta = 0
limiteConta = 500
extratoConta = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que quer depositar: "))

        if valor > 0:
            saldoConta += valor
            extratoConta += f"Valor: R$ {valor:.2f}\n"

        else:
            print("Valor é inválido")

    elif opcao == "s":
        valor = float(input("Digite o valor para retirar"))

        excedeu_saldo = valor > saldoConta

        excedeu_limite = valor > limiteConta

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Sem saldo")

        elif excedeu_limite:
            print("Saque ultrapassa o limite.")

        elif excedeu_saques:
            print("Numero de saques atingidos.")

        elif valor > 0:
            saldoConta -= valor
            extratoConta += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor é inválido")

    elif opcao == "e":
        print(f"\nSaldo: R$ {saldoConta:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, efetue novamente")
