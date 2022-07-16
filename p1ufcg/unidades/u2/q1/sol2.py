cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

ultimos_digitos1 = cpf1 % 100
cpf1_unidades = ultimos_digitos1 % 10
cpf1_dezenas = ultimos_digitos1 // 10

ultimos_digitos2 = cpf2 % 100
cpf2_unidades = ultimos_digitos2 % 10
cpf2_dezenas = ultimos_digitos2 // 10

ultimos_digitos3 = cpf3 % 100
cpf3_unidades = ultimos_digitos3 % 10
cpf3_dezenas = ultimos_digitos3 // 10

soma1 = cpf1_dezenas + cpf1_unidades
soma2 = cpf2_dezenas + cpf2_unidades
soma3 = cpf3_dezenas + cpf3_unidades

print(soma1, soma2, soma3)
