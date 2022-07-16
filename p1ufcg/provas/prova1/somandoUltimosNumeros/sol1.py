# coding: utf-8
# PROG1 - UFCG
# ALUNO: João Pedro Juvino dos Santos | DATA : 14/02/2022 | MATRÍCULA: 121110319
# EXERCÍCIO: Somando os últimos números

# |ENTRADA(S)| e |PROCESSAMENTO|
qtd_de_numeros = int(input())

lista_de_numeros = []
soma_dos_numeros = 0
for entrada in range(qtd_de_numeros):
    valor_da_entrada = int(input())
    lista_de_numeros.append(valor_da_entrada)
    soma_dos_numeros += valor_da_entrada

media_de_numeros = soma_dos_numeros / qtd_de_numeros

soma_dos_ultimos = 0
ultimo_indice = qtd_de_numeros - 1
for indice in range(ultimo_indice, -1, -1):
    if(lista_de_numeros[indice] >= media_de_numeros):
        soma_dos_ultimos += lista_de_numeros[indice]
        break
    soma_dos_ultimos += lista_de_numeros[indice]

# |SAÍDA(S)|
print(soma_dos_ultimos)
