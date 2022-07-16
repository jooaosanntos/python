from math import pi

if __name__ == "__main__":
    raio = float(input())

    area_circulo = pi * raio ** 2

    lado_quadrado_inscrito = (raio * 2 / 2 ** (1 / 2))
    area_quadrado_inscrito = lado_quadrado_inscrito ** 2

    area_nao_comum = area_circulo - area_quadrado_inscrito

    print(f"Área não comum: {area_nao_comum:.5f}")

