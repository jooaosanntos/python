valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 >= valor2:
    aux = valor1
    valor1 = valor2
    valor2 = aux
if valor3 >= valor2:
    aux = valor3
    valor3 = valor2
    valor2 = aux
if valor3 >= valor1:
    aux = valor3
    valor3 = valor2
    valor2 = aux
print(valor1, valor2, valor3)
