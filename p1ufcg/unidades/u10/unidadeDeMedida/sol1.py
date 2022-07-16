def somar_valores(valor1, unidade1, valor2, unidade2, unidades):
    
    valor1_convertido = int(valor1) * unidades[unidade1]
    valor2_convertido = int(valor2) * unidades[unidade2]

    soma = valor1_convertido + valor2_convertido

    return soma


if __name__ == "__main__":

    unidades = {
        "km": 1000,
        "hm": 100,
        "dam": 10,
        "m": 1,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    }

    while True:
        valor1, unidade1, valor2, unidade2 = input().split(" ")
        
        if valor1 == "0" and valor2 == "0": break
        
        soma_final = somar_valores(valor1, unidade1, valor2, unidade2, unidades)

        print(f"{soma_final:.2f} m")

