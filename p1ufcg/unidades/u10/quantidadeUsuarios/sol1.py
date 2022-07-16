def quantidade_usuarios(cadastro):
    quantidade_pessoas = 0
    for chave in cadastro.keys():
        if chave != 9999:
            for pessoa in cadastro[chave]:
                quantidade_pessoas += 1

    return quantidade_pessoas

