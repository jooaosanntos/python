valor = int(input("Valor: "))

soma = 0
ctt = 0

while valor > 0:
    soma += valor
    ctt += 1
    valor = int(input("Valor: "))

media = soma / ctt

print(media)
