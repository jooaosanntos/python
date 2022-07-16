def achar_indice(caractere, lista_letras):
    for indice in range(len(lista_letras)):
        if lista_letras[indice] == caractere:
            return indice
    return -1
            

def is_substring(str1, str2):
    lista1 = list(str1)
    
    for letra in str2:
        indice = achar_indice(letra, lista1)
        if indice == -1: return False
        else:
            lista1.pop(indice)

    return True

