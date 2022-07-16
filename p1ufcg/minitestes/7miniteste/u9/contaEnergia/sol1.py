def calcula_conta(tabela):
    valor_consumo = 0
    for indice in range(1, len(tabela)):
        valor_consumo += tabela[indice][1] * tabela[indice][2] * tabela[indice][3]

    valor_reais = (valor_consumo / 1000) * 0.28

    return f"R$ {valor_reais:.2f}"

