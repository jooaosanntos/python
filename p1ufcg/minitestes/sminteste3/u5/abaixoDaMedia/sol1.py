lista_num = []
soma = 0
while True:
    valor = input()
    if valor == "fim": break
    valor = int(valor)
    lista_num.append(valor)
    soma += valor

tam_lista_num = len(lista_num)
media = soma / tam_lista_num
print(f"{media:.2f}")
for index in range(tam_lista_num):
    if lista_num[index] < media:
        posicao = index + 1
        print(posicao, lista_num[index])
