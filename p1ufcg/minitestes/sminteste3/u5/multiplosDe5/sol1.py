num = int(input())

valor = 10
while valor < num:
    if valor % 5 == 0 and valor % 2 == 0:
        print(valor)
        valor += 10
    else:
        valor += 5

