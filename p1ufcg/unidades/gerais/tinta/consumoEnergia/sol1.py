# coding: utf-8
# Calculando o consumo de energia em Joules

if __name__ == "__main__":

    potencia  = int(input())
    tempo = int(input())

    consumo = (potencia * tempo) / 60000

    print(f"{consumo:.1f} kWh")


