def pegar_diagonal_secundaria(M):
    diagonal_secundaria = []

    indice_linha = 0
    for indice_coluna in range(len(M[0]) - 1, -1, -1):
        
        diagonal_secundaria.append(M[indice_linha][indice_coluna])
        indice_linha += 1

    return diagonal_secundaria


def pegar_diagonal_principal(M):
    diagonal_principal = []

    for indice_linha in range(len(M)):

        for indice_coluna in range(len(M[0])):

            if indice_linha == indice_coluna:
                diagonal_principal.append(M[indice_linha][indice_coluna])

    return diagonal_principal


def diagonais(M):
    
    diagonal_principal = pegar_diagonal_principal(M)
    diagonal_secundaria = pegar_diagonal_secundaria(M)

    matriz_final = [diagonal_principal, diagonal_secundaria]

    return matriz_final


