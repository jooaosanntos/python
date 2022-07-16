def eh_chave(dicionario, chave_pretendida):
    for chave in dicionario.keys():
        if chave == chave_pretendida:
            return True
    return False

def criar_semelhante(dicionario):
    novo_dicionario = {}
    for chave in dicionario.keys():
        novo_dicionario[chave] = dicionario[chave]

    return novo_dicionario

def balanco(estoque1, estoque2):
    balanco_final = criar_semelhante(estoque1)
    for chave2 in estoque2.keys():
        if eh_chave(balanco_final, chave2):
            balanco_final[chave2] += estoque2[chave2]
        else:
            balanco_final[chave2] = estoque2[chave2]
            
    return balanco_final

