vendedor = input("Qual é o nome do(a) vendedor(a)? ")
valor_da_venda = float(input("Qual é o valor da venda? "))

comissao1 = valor_da_venda * 0.05
comissao2 = valor_da_venda * 0.1

if valor_da_venda <= 500:
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor} é R$ {comissao1:.2f}.")
else:
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor:.5s} é R$ {comissao2:.2f}.")

