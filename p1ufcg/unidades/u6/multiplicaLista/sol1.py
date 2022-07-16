def multiplica_lista(fator, lista_atual):
    nova_lista = []
    for qtd_vezes in range(fator):
        for elemento in lista_atual:
            nova_lista.append(elemento)

    return nova_lista

