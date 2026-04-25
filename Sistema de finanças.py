transacoes = []

def adicionar_transacao():
    tipo = input("Digite o tipo da transação (entrada/saída): ")
    valor = float(input("Digite o valor da transação: "))
    descricao = input("Digite a descrição da transação: ")
    
    transacao = {
        "tipo": tipo,
        "valor": valor,
        "descricao": descricao
    }
    transacoes.append(transacao)

def exibir_transacoes():
    for transacao in transacoes:
        print(f"{transacao['tipo'].capitalize()}: R${transacao['valor']:.2f} - {transacao['descricao']}") 

def calcular_saldo():
    saldo = 0
    for transacao in transacoes:
        if transacao["tipo"] == "entrada":
            saldo += transacao["valor"]
        elif transacao["tipo"] == "saída":
            saldo -= transacao["valor"]
    return saldo    

def main():
    while True:
        print("\n1. Adicionar Transação")
        print("2. Exibir Transações")
        print("3. Calcular Saldo")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar_transacao()
        elif escolha == "2":
            exibir_transacoes()
        elif escolha == "3":
            saldo = calcular_saldo()
            print(f"Saldo atual: R${saldo:.2f}")
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()  

    print("Programa encerrado. Obrigado por usar o sistema de finanças!")