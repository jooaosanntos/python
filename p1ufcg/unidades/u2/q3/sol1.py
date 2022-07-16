import math
capacidade_revestimento = float(input("Capacidade de revestimento? "))

print("\n== Dados do vão a revestir ==")

comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

area = (comprimento * altura + largura * altura) * 2 + comprimento * largura
num_caixas = math.ceil(area / capacidade_revestimento)

print("\n== Resultados ==")

print(f"Área total a revestir: {area:.1f} m2")
print(f"Número de caixas: {num_caixas}")
