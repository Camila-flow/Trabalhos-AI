def calculadora():
    lista_historico = []  # Inicializa a lista para o histórico

        #Escolher operacao para ser efetuada pela calculadora
    while True:
        op = input("Digite a operação (soma, subtracao, multi, div, hist ou sair): ").strip().lower()
        if op not in ["soma", "hist", "subtracao", "div", "multi", "sair"]:
            print("operacao invalida")
            continue

        if op == "sair":
            break
        if op != "hist":
        #Após escolher operacao escolher dois numeros para ser feita a conta
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            
        #Efetua a operacao de soma com os dois numeros escolhidos e mostra a conta por extenso
        if op == "soma":
            result = num1 + num2
            conta = str(num1) + " + " + str(num2) + " = " + str(result)
            print(conta)
            lista_historico.append(conta)
            
        #Efetua a operacao de multiplicacao com os dois numeros escolhidos e mostra a conta por extenso
        elif op == "multi":
            result = num1 * num2
            conta = str(num1) + " * " + str(num2) + " = " + str(result)
            print(conta)
            lista_historico.append(conta)
            
        #Efetua a operacao de subtracao com os dois numeros escolhidos e mostra a conta por extenso
        elif op == "subtracao":
            result = num1 - num2
            conta = str(num1) + " - " + str(num2) + " = " + str(result)
            print(conta)
            lista_historico.append(conta)
            
       #Efetua a operacao de divisao com os dois numeros escolhidos e mostra a conta por extenso
        elif op == "div":
            result = num1 / num2
            conta = str(num1) + " / " + str(num2) + " = " + str(result)
            print(conta)
            lista_historico.append(conta)
            
         #Mostra o historico da calculadora
        elif op == "hist":
            print("Histórico das últimas 5 operações:")
            for i, operacao in enumerate(lista_historico[-5:], 1):
                print(str(operacao))

        # Mantém apenas as últimas 5 operações no histórico
        if len(lista_historico) > 5:
            lista_historico.pop(0)

calculadora()

