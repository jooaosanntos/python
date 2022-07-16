cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

cpf1_parte1 = int(cpf1 / 100)
cpf1_parte2 = cpf1 - (cpf1_parte1 * 100)

cpf1_parte2_dezena = int(cpf1_parte2 / 10)
cpf1_parte2_unidade = cpf1_parte2 - (cpf1_parte2_dezena * 10)
cpf1_parte2_soma = cpf1_parte2_dezena + cpf1_parte2_unidade

cpf2_parte1 = int(cpf2 / 100)
cpf2_parte2 = cpf2 - (cpf2_parte1 * 100)

cpf2_parte2_dezena = int(cpf2_parte2 / 10)
cpf2_parte2_unidade = cpf2_parte2 - (cpf2_parte2_dezena * 10)
cpf2_parte2_soma = cpf2_parte2_dezena + cpf2_parte2_unidade 

cpf3_parte1 = int(cpf3 / 100)
cpf3_parte2 = cpf3 - (cpf3_parte1 * 100)

cpf3_parte2_dezena = int(cpf3_parte2 / 10)
cpf3_parte2_unidade = cpf3_parte2 - (cpf3_parte2_dezena * 10)
cpf3_parte2_soma = cpf3_parte2_dezena + cpf3_parte2_unidade 

print(f"{cpf1_parte1}-{cpf1_parte2}")
print(cpf1_parte2_soma)

print(f"{cpf2_parte1}-{cpf2_parte2}")
print(cpf2_parte2_soma)

print(f"{cpf3_parte1}-{cpf3_parte2}")
print(cpf3_parte2_soma)
