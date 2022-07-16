lista_entradas = []
soma_entradas = 0
qtd_entradas = 0
while True:
    entrada = int(input())
    soma_provavel = soma_entradas + entrada
    if soma_provavel > 100 or entrada < 0: break
    lista_entradas.append(entrada)
    soma_entradas += entrada
    qtd_entradas += 1

media_entradas = soma_entradas / qtd_entradas

for index in range(len(lista_entradas)):
    if lista_entradas[index] > media_entradas:
        print(f"{lista_entradas[index]} > {media_entradas:.3f}")
    elif lista_entradas[index] < media_entradas:
        print(f"{lista_entradas[index]} < {media_entradas:.3f}")
