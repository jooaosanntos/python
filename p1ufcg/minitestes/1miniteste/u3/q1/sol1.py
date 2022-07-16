record = float(input())
qtd_comida = float(input())

if record < qtd_comida:
    print(f"recorde quebrado ({qtd_comida:.2f} kg)")
elif record > qtd_comida:
    print("recorde mantido")
else:
    print("recorde empatado")
