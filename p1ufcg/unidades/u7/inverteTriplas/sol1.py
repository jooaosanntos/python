def organizar3a3(s):
    
    lista_3a3 = []
    palavra_3a3 = ""
    for indice in range(len(s)):
        palavra_3a3 += s[indice]
        if len(palavra_3a3) == 3:
            lista_3a3.append(palavra_3a3)
            palavra_3a3 = ""
    
    return lista_3a3

def meu_join(lista):
    palavra = ""
    for caractere in lista:
        palavra += caractere
    return palavra

def inverte3a3(s):
    lista3a3 = organizar3a3(s)

    indice_inicial = 0
    indice_final = len(lista3a3) - 1
    while True:
        if indice_inicial >= indice_final: break

        lista3a3[indice_inicial], lista3a3[indice_final] = lista3a3[indice_final], lista3a3[indice_inicial]

        indice_inicial += 1

        indice_final -= 1
    palavra_alterada = meu_join(lista3a3)
    return palavra_alterada

