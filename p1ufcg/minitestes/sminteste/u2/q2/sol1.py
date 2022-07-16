import math
lado_quadrado = float(input())

raio = (lado_quadrado * (2 ** (1/2))) / 2

perimetro_circunferencia = math.pi * raio * 2
area_circunferencia = math.pi * (raio ** 2)

print(f"Perímetro: {perimetro_circunferencia:.5f}")
print(f"Área: {area_circunferencia:.5f}")
