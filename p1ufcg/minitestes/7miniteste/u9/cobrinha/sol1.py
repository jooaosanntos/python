def eh_impar(valor):
    return valor % 2 != 0

def cobrinha(M):
    lista_impares = []
    cobrinha = 0
    for indice_linha  in range(len(M)):
        if cobrinha == 0:
            for indice_coluna in range(len(M[0])):
                if eh_impar(M[indice_linha][indice_coluna]):
                    lista_impares.append(M[indice_linha][indice_coluna])
            cobrinha = -1
        elif cobrinha == -1:
            for indice_coluna in range(len(M[0]) - 1, -1, -1):
                if eh_impar(M[indice_linha][indice_coluna]):
                    lista_impares.append(M[indice_linha][indice_coluna])
            cobrinha = 0

    return lista_impares

