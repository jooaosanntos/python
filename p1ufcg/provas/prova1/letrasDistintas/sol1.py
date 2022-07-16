# coding: utf-8
# PROG1 - UFCG
# ALUNO: João Pedro Juvino dos Santos | DATA : 14/02/2022 | MATRÍCULA: 121110319
# EXERCÍCIO: Letras distintas

# |ENTRADA(S)|
palavra1 = input()
palavra2 = input()

# |PROCESSAMENTO|
numero_de_distintas = 0
for letra_palavra1 in palavra1:
    distinta = True
    for letra_palavra2 in palavra2:
        if letra_palavra1 == letra_palavra2:
            distinta = False
            break
    if distinta:
        numero_de_distintas += 1

# |SAÍDA(S)|
print(numero_de_distintas)
