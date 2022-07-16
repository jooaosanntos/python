# coding: utf-8
# CURSO: Bacharelado em Ciência da Computação - Universidade Federal de Campina Grande
# DISCIPLINA: Programação 1
# ALUNO: João Pedro Juvino dos Santos | DATA : 30/03/2022 | MATRÍCULA: 121110319
# Prova de reposição
# EXERCÍCIO: Filtra linhas inválidas

# |ENTRADA(S)| e |PROCESSAMENTO| e |SAÍDA(S) INICIAL(IS)|
def eh_invalida(lista):
    qtd_par = 0
    qtd_impar = 0
    for elemento in lista:
        if elemento % 2 == 0: qtd_par += 1
        else: qtd_impar += 1
    return qtd_impar > qtd_par


qtd_entradas = 0
qtd_invalidas = 0
while True:
    entrada = input()
    if entrada == "fim": break
    
    qtd_entradas += 1

    lista_entradas = entrada.split(" ")

    sequencia_numeros = [int(valor) for valor in lista_entradas]

    if eh_invalida(sequencia_numeros):
        qtd_invalidas += 1
        print(f"linha {qtd_entradas} inválida: {entrada}")

# |SAÍDA FINAL|
print(f"sequências lidas: {qtd_entradas} (inválidas: {qtd_invalidas})")

