qtd_entradas = int(input())

lista_entradas = []
for n in range(qtd_entradas):
    entrada = int(input())
    lista_entradas.append(entrada)

print("---")

menor_valor = int(input())
maior_valor = int(input())

qtd_valores_antes = 0
qtd_valores_entre = 0
qtd_valores_depois = 0
for index in range(qtd_entradas):
    if lista_entradas[index] > maior_valor:
        qtd_valores_depois += 1
    elif lista_entradas[index] < menor_valor:
        qtd_valores_antes += 1
    elif lista_entradas[index] < maior_valor and lista_entradas[index] > menor_valor:
        qtd_valores_entre += 1

print(qtd_valores_antes, "antes")
print(qtd_valores_entre, "entre")
print(qtd_valores_depois, "depois")
