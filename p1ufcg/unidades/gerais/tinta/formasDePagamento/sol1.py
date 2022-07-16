if __name__ == "__main__":
    
    tamanho_terreno = float(input())
    valor_metro = float(input())
    opcao_pagamento = input()

    if opcao_pagamento == "vista":
        valor_total = (tamanho_terreno * valor_metro) * 0.8
        print(f"Total: R$ {valor_total:.2f}")

    elif opcao_pagamento == "2x":
        valor_total = (tamanho_terreno * valor_metro) * 0.9
        valor_parcelas = valor_total / 2
        print(f"Total: R$ {valor_total:.2f}. Parcelas: R$ {valor_parcelas:.2f}")

    elif opcao_pagamento == "3x":
        valor_total = (tamanho_terreno * valor_metro) * 0.95
        valor_parcelas = valor_total / 3
        print(f"Total: R$ {valor_total:.2f}. Parcelas: R$ {valor_parcelas:.2f}")

