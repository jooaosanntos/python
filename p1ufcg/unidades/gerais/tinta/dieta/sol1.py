if __name__ == "__main__":

    qtd_perder = float(input())
    tempo_exercicios = float(input())
    qtd_ganha = float(input())

    # Quantidade que quer perder
    qtd_perder_cal = qtd_perder * 7700

    # Quantidade perdida
    qtd_perdidas_cal = tempo_exercicios * 900

    # Saldo diário
    saldo_diario = qtd_perdidas_cal+ 2000 - qtd_ganha

    # Tempo estipulado
    qtd_dias = qtd_perder_cal / saldo_diario
    
    print(f"Você precisará de {qtd_dias:.2f} dias de dieta")

