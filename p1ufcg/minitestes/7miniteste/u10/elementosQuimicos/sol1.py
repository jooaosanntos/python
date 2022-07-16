tabela_elementos = {
        "H": 1,
        "S": 32,
        "O": 16,
        "C": 12,
        "Ca": 40,
        "Na": 23,
        "P": 31
}

while True:
    elemento = input().split(" ")
    if elemento[0] == "fim": break
    soma = 0
    for indice in range(len(elemento) - 1):
        valor_massa = 0
        if not elemento[indice].isdigit():
            elemento_atual = tabela_elementos[elemento[indice]]
            if elemento[indice + 1].isdigit():
                elemento_atual *= int(elemento[indice + 1])
            valor_massa = elemento_atual
        soma += valor_massa

    if not (elemento[len(elemento) - 1].isdigit()):
        soma += tabela_elementos[elemento[len(elemento) - 1]]

    print(soma)

