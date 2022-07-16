def maioridade_penal(frase_de_pessoas, frase_de_idades):
    maiores_de_idade = ""

    lista_de_pessoas = frase_de_pessoas.split(" ")
    lista_de_idades = frase_de_idades.split(" ")

    for indice in range(len(lista_de_idades)):
        if int(lista_de_idades[indice]) >= 18:
            if len(maiores_de_idade) > 0:
                maiores_de_idade += f" {lista_de_pessoas[indice]}"
            else:
                maiores_de_idade += f"{lista_de_pessoas[indice]}"

    return maiores_de_idade

