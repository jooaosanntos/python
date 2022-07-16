# coding: utf-8
# PROG1 - UFCG
# ALUNO: JOÃO PEDRO JUVINO DOS SANTOS | DATA : 12/02/2022 | MATRÍCULA: 121110319
# EXERCICIO: Graus Decimais

# |ENTRADA(S)|
graus = int(input())
minutos = int(input())
segundos = int(input())

# |PROCESSAMENTO|
decimais = (minutos / 60) + (segundos / 3600)
graus += decimais

# |SAÍDA(S)|
print(f"graus = {graus:.4f}")
