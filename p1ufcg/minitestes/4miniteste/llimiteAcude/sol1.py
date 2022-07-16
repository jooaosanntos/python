limite_superior = float(input())
qtd_atual = float(input())

while qtd_atual < limite_superior:
    tipo, qtd = input().split()
    qtd = int(qtd)
    if tipo == "chuva" or tipo == "afluente":
        qtd_atual += qtd
    final = qtd_atual - qtd
    if tipo == "demanda" and final >= 0:
        qtd_atual = final
print("Açude passou a liberar água.")
print(f"Nível: {qtd_atual:.2f}")
