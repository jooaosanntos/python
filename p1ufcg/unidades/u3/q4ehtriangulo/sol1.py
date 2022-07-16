a = int(input())
b = int(input())
c = int(input())
    
soma = a + b + c

if a < b + c and a > ((b - c) ** 2) ** 0.5:
    if b < a + c and b > ((a - c) ** 2) ** 0.5:
        if c < b + a and c > ((b - a) ** 2) ** 0.5:
            print(f"triangulo valido. {soma}")
else:
    print("triangulo invalido.")
