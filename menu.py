def menu():
    while True:
        print("\n1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("Saindo...")
            break

        elif opcao == 1:
            print("Você escolheu Somar")
        elif opcao == 2:
            print("Você escolheu Subtrair")
        elif opcao == 3:
            print("Você escolheu Multiplicar")
        elif opcao == 4:
            print("Você escolheu Dividir")
        else:
            print("Opção inválida!")
menu()