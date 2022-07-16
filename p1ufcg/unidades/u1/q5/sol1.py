numero_adultos = int(input())
numero_criancas = int(input())
preco_ingresso = float(input())

valor_cobrado = (numero_adultos * preco_ingresso) + (numero_criancas * preco_ingresso / 2)

print(f"Total: R$ {valor_cobrado:.2f}")
