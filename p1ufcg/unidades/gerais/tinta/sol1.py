if __name__ == "__main__":
    altura_parede = float(input())
    largura_parede = float(input())

    area_parede = altura_parede * largura_parede

    quantidade_litros = (area_parede * 3.6) / 50

    print(f"{quantidade_litros:.2f} l")
