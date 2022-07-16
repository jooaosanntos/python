posicao_inicial = input().split(" ")
y = int(posicao_inicial[1])
x = int(posicao_inicial[0])

deslocamento_total = 0
while True:
    entrada_movimentos = input()
    if entrada_movimentos == "X": break

    direcao = entrada_movimentos.split(" ")[0]
    qtd_movimento = int(entrada_movimentos.split(" ")[1])

    if direcao == "C":
        y -= qtd_movimento
    elif direcao == "B":
        y += qtd_movimento
    elif direcao == "D":
        x += qtd_movimento
    else:
        x -= qtd_movimento

    deslocamento_total += qtd_movimento

    print(f"> {y} {x}")

print(deslocamento_total)
