# Entrada
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

peso1 = float(input())
peso2 = float(input())

# Processamento
peso3 = 100 - peso1 - peso2

media_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / 100

# Saída
print(f"Média Final: {media_final:.1f}")
