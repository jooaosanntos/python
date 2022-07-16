def busca_matriz(m, e):
    lista_indices = []

    for indice_linha in range(len(m)):
        
        for indice_coluna in range(len(m[indice_linha])):

            if m[indice_linha][indice_coluna] == e:
                tupla_indices = tuple([indice_linha, indice_coluna])
                lista_indices.append(tupla_indices)

    return lista_indices

