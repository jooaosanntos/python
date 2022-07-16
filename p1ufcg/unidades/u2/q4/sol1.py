import math

print("Cálculo da Superfície de um Cilindro")

print("---")
diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))
print("---")

area_retangulo = 2 * math.pi * (diametro / 2) * altura
area_circulos = 2 * (math.pi * (diametro / 2) ** 2)
area = area_retangulo + area_circulos

print(f"Área calculada: {area:.2f}")
