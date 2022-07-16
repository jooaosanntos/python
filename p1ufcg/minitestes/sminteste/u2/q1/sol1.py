qtd_morangos = int(input())

qtd_caixas = qtd_morangos // 400

qtd_sobras = qtd_morangos - (qtd_caixas * 400)
porcentagem_sobras = (qtd_sobras / qtd_morangos) * 100

print(f"{qtd_caixas} caixa(s) completa(s) para embalar os morangos.")
print(f"{porcentagem_sobras:.1f}% dos morangos serão perdidos.")
