def tratar_erro(valor, opcoes):
    while True:
        if valor in opcoes:
            break
        else:
            print('='*40)
            print("Digite um valor válido")
            print('='*40)
            valor = input('Escolha: ')

    return valor
