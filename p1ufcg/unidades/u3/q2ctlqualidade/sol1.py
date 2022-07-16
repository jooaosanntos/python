peso_antes = float(input())
peso_depois = float(input())

porcentagem_agua = ((peso_antes - peso_depois) / peso_antes) * 100

print(f"{porcentagem_agua:.1f}% do peso do produto é de água congelada.")
if porcentagem_agua < 10:
    if porcentagem_agua < 5:
        print("Produto qualis A.")
    else:
        print("Produto em conformidade.")
else:
    print("Produto não conforme.")
