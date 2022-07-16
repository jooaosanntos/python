area_construida = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

iptu = area_construida * aliquota + 35

opcao1 = iptu * 0.75

opcao2 = iptu * 0.95
opcao2_parcelas = opcao2 / 6

opcao3_parcelas = iptu / 10

print(f"IPTU: R$ {iptu:.2f}\n")

print("Pagamento:")
print(f"1. Quota única. R$ {opcao1:.2f}")

print(f"2. Em 6 parcelas. Total: R$ {opcao2:.2f}\n   6 x R$ {opcao2_parcelas:.2f}")

print(f"3. Em 10 parcelas. Total: R$ {iptu:.2f}\n   10 x R$ {opcao3_parcelas:.2f}")
