def eh_chave(chave_pretendida, dicionario):
    for chave in dicionario.keys():
        if chave == chave_pretendida:
            return True
    return False


def decifra(chave, mensagem):
    palavra_decodificada = ""
    for letra in mensagem:
        if eh_chave(letra, chave):
            palavra_decodificada += chave[letra]
        else:
            palavra_decodificada += letra
    return palavra_decodificada


