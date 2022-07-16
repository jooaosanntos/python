numb = input()

numd = 0

inicio = len(numb) - 1
index = 0
for pot in range(inicio, -1, -1):
    numb_int = int(numb[index])
    potencia = 2 ** (pot)
    operacao_atual = numb_int * potencia
    numd += operacao_atual
    index += 1
    print(f"{numb_int} * {potencia} = {operacao_atual}")

print(f"{numb}(2) = {numd}(10)")
