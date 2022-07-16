def esta_presente(valor, array):
    for elemento in array:
        if elemento == valor: return True
    return False

if __name__ == "__main__":
    
    valores_pedagio = {
            "Automóvel utilitário": [11.4, "sem_eixos"],
            "Ônibus": [11.4, "com_eixos"],
            "Caminhão": [9.6, "com_eixos"],
            "Motocicleta": [5.7, "sem_eixos"]
    }
    
    veiculo = input()

    if esta_presente(veiculo, valores_pedagio.keys()):
        valor_total = 0
        if valores_pedagio[veiculo][1] == "com_eixos":
            quantidade_eixos = int(input())
            valor_total = valores_pedagio[veiculo][0] * quantidade_eixos
        elif valores_pedagio[veiculo][1] == "sem_eixos":
            valor_total = valores_pedagio[veiculo][0]
        print(f"Valor a pagar: R$ {valor_total:.2f}.")
    else:
        print("Veículo não cadastrado.")
