# Área de uma esfera
# coding: utf-8
# PROG1 - UFCG
# ALUNO: JOÃO PEDRO JUVINO DOS SANTOS | DATA : 08/02/2022 | MATRICULA: 121110319
# EXERCÍCIO: Esfera

# |ENTRADAS|
from math import pi
raio = float(input())

# |PROCESSAMENTO|
area = 4 * pi * (raio ** 2)
volume = (4 * pi * (raio ** 3)) / 3

# |SAIDA|
print(f"{area:.2f}")
print(f"{volume:.2f}")

