# coding: utf-8
# PROG1 - UFCG
# ALUNO: JOÃO PEDRO JUVINO DOS SANTOS | DATA : 12/02/2022 | MATRÍCULA: 121110319
# EXERCICIO: Lucro Mensal

# |ENTRADA(S) E PROCESSAMENTO|
lista = []
for n in range(12):
    valor1, valor2 = input().split(" ")
    valor1 = float(valor1)
    valor2 = float(valor2)

    lucro = valor1 - valor2
    lista.append(lucro)

# |SAÍDA(S)|
for index in range(12):
    if index == 0:
        print(f"jan{lista[index]:5.1f}")
    elif index == 1:
        print(f"fev{lista[index]:5.1f}")
    elif index == 2:
        print(f"mar{lista[index]:5.1f}")
    elif index == 3:
        print(f"abr{lista[index]:5.1f}")
    elif index == 4:
        print(f"mai{lista[index]:5.1f}")
    elif index == 5:
        print(f"jun{lista[index]:5.1f}")
    elif index == 6:
        print(f"jul{lista[index]:5.1f}")
    elif index == 7:
        print(f"ago{lista[index]:5.1f}")
    elif index == 8:
        print(f"set{lista[index]:5.1f}")
    elif index == 9:
        print(f"out{lista[index]:5.1f}")
    elif index == 10:
        print(f"nov{lista[index]:5.1f}")
    elif index == 11:
        print(f"dez{lista[index]:5.1f}")
