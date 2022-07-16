tensao_corrente1 = float(input())
resistencia_corrente1 = float(input())

tensao_corrente2 = float(input())
resistencia_corrente2 = float(input())

tensao_corrente3 = float(input())
resistencia_corrente3 = float(input())

corrente1 = tensao_corrente1 / resistencia_corrente1
corrente2 = tensao_corrente2 / resistencia_corrente2
corrente3 = tensao_corrente3 / resistencia_corrente3

if corrente1 >= corrente2 and corrente1 >= corrente3:
    print("condutor com maior corrente: 1")
    if corrente1 >= 1:
        print(f"maior corrente: {corrente1:.2f} A")
    elif corrente1 >= 0.001:
        corrente1 *= 1000
        print(f"maior corrente: {corrente1:.2f} mA")
    else:
        corrente1 *= 1000000
        print(f"maior corrente: {corrente1:.2f} µA")
elif corrente2 > corrente1 and corrente2 > corrente3:
    print("condutor com maior corrente: 2")
    if corrente2 >= 1:
        print(f"maior corrente: {corrente2:.2f} A")
    elif corrente2 >= 0.001:
        corrente2 *= 1000
        print(f"maior corrente: {corrente2:.2f} mA")
    else:
        corrente2 *= 1000000
        print(f"maior corrente: {corrente2:.2f} µA")
else:
    print("condutor com maior corrente: 3")
    if corrente3 >= 1:
        print(f"maior corrente: {corrente3:.2f} A")
    elif corrente3 >= 0.001:
        corrente3 *= 1000
        print(f"maior corrente: {corrente3:.2f} mA")
    else:
        corrente3 *= 1000000
        print(f"maior corrente: {corrente3:.2f} µA")

