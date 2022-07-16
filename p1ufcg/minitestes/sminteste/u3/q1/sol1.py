valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 >= valor2 and valor1 >= valor3:
    if valor2 >= valor3:
        maior1 = valor1
        maior2 = valor2
        maior3 = valor3
    else:
        maior1 = valor1
        maior2 = valor3
        maior3 = valor2
elif valor2 >= valor1 and valor2 >= valor3:
    if valor1 >= valor3:
        maior1 = valor2
        maior2 = valor1
        maior3 = valor3
    else:
        maior1 = valor2
        maior2 = valor3
        maior3 = valor1
else:
    if valor2 >= valor1:
        maior1 = valor3
        maior2 = valor2
        maior3 = valor1
    else:
        maior1 = valor3
        maior2 = valor1
        maior3 = valor2

print(maior3, maior2, maior1)
