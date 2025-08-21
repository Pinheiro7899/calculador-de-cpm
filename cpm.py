# Sistema para calcular CPM com base no documento 4.2.txt

# Lista para armazenar o histórico de cálculos
historico_cpm = []

def calcular_cpm(custo, impressoes):
    """
    Função que calcula o CPM usando a fórmula: (custo / impressoes) * 1000
    """
    if impressoes == 0:  # Operador de comparação para evitar divisão por zero
        return None
    cpm = (custo / impressoes) * 1000  # Operadores aritméticos
    return round(cpm, 2)  # Arredonda para 2 casas decimais

# Laço principal
while True:  # Laço while para permitir múltiplos cálculos
    print("\n=== Calculadora de CPM ===")
    print("1. Calcular novo CPM")
    print("2. Exibir histórico de cálculos")
    print("3. Sair")

    opcao = input("Escolha uma opção (1, 2 ou 3): ")

    if opcao == "1":  # Condicional if para calcular CPM
        try:
            custo = float(input("Digite o custo total da campanha (R$): "))
            impressoes = float(input("Digite o número de impressões: "))
            
            # Validação usando operadores de comparação
            if custo < 0 or impressoes < 0:
                print("Erro: Custo e impressões devem ser valores não negativos.")
                continue  # Pula para a próxima iteração do laço
            
            resultado = calcular_cpm(custo, impressoes)
            if resultado is None:
                print("Erro: Número de impressões não pode ser zero.")
                continue
            
            # Adiciona resultado à lista (método append)
            historico_cpm.append({"custo": custo, "impressoes": impressoes, "cpm": resultado})
            print(f"O CPM é: R${resultado}")
        
        except ValueError:
            print("Erro: Digite valores numéricos válidos.")
            continue
    
    elif opcao == "2":  # Condicional elif para exibir histórico
        if len(historico_cpm) == 0:  # Operador de comparação
            print("Nenhum cálculo no histórico.")
        else:
            print("\n=== Histórico de Cálculos ===")
            for i, calc in enumerate(historico_cpm, 1):  # Laço for para iterar lista
                print(f"Cálculo {i}: Custo = R${calc['custo']}, Impressões = {calc['impressoes']}, CPM = R${calc['cpm']}")
    
    elif opcao == "3":  # Condicional elif para sair
        print("Saindo do programa...")
        break  # Interrompe o laço while
    
    else:
        print("Opção inválida. Tente novamente.")
        continue  # Pula para a próxima iteração
    
    # Placeholder para funcionalidades futuras
    pass  # Instrução pass como marcador


