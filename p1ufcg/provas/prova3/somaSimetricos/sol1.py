# coding: utf-8
# CURSO: Bacharelado em Ciência da Computação - Universidade Federal de Campina Grande
# DISCIPLINA: Programação 1
# ALUNO: João Pedro Juvino dos Santos | DATA : 30/03/2022 | MATRÍCULA: 121110319
# Prova de reposição
# EXERCÍCIO: Soma simétricos

# |PROCESSAMENTO DA QUESTÃO|
def soma_simetricos(valores):  
    lista_soma = []
     
    indice_inicial = 0
    indice_final = len(valores) - 1
    while True:    
        if indice_inicial > indice_final: break
        elif indice_inicial == indice_final:
            lista_soma.append(valores[indice_inicial])
            break

        soma = valores[indice_inicial] + valores[indice_final]
        lista_soma.append(soma)
        
        indice_inicial += 1
        indice_final -= 1

    return lista_soma

## Testes

# Teste para quantidade par de valores de entrada
def test_1():
    assert soma_simetricos([4, 5, 6, 9]) == [13, 11]

# Teste para quantidade impar de valores de entrada
def test_2():
    assert soma_simetricos([4, 5, 6, 9, 4]) == [8, 14, 6]

# Tese com um único valor de entrada
def test_3():
    assert soma_simetricos([3]) == [3]

# Teste sem valores de entrada
def test_4():
    assert soma_simetricos([]) == []

# Teste para valores negativos de entrada
def test_5():
    assert soma_simetricos([-1, -2, -3]) == [-4, -2]

# Teste para valores iguais de entrada
def test_6():
    soma_simetricos([1,1,1,1,1,1,1,1]) == [2,2,2,2]

# Teste para valores nulos de entrada
def test_7():
    assert soma_simetricos([0,0,0,0,0]) == [0,0,0]


