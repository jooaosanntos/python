qtd = int(input())

soma_pares = 0
qtd_pares = 0
lista_pares = []
for n in range(qtd):
    
    entrada = int(input())
    
    if entrada % 2 == 0:
        soma_pares += entrada
        qtd_pares += 1
    
    lista_pares.append(entrada)

media_pares = soma_pares / qtd_pares

qtd_acima_media = 0
for index in range(qtd):
    if lista_pares[index] > media_pares:
        qtd_acima_media += 1

print(f"média dos pares: {media_pares:.1f}")
print(f"acima da média: {qtd_acima_media}")
