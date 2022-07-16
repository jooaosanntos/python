def calcula_digitos_verificacao(cpf, codigo=""):
    if len(codigo) == 2:
        return codigo
    
    fator_de_multiplicacao = 2
    somatorio = 0
    for index in range(len(cpf) - 1, -1, -1):
        somatorio += (int(cpf[index]) * fator_de_multiplicacao)
        fator_de_multiplicacao += 1
    
    primeiro_digito = (somatorio * 10) % 11
    codigo += f"{primeiro_digito}"
    novo_cpf = cpf + f"{primeiro_digito}"

    return calcula_digitos_verificacao(novo_cpf, codigo)
