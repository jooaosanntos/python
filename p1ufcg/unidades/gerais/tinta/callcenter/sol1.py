if __name__ == "__main__":
    soma = 0
    for rep in range(7):
        entrada = int(input())
        soma += entrada
    media = soma / 7

    print(f"Total: {soma}")
    print(f"Média: {media:.2f}")
