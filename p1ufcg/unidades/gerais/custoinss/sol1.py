salario = float(input())

inss_empregador = salario * 0.12

if salario > 2195.12:
    inss_empregado = salario * 0.11
elif salario > 1317.07:
    inss_empregado = salario * 0.09
else:
    inss_empregado = salario * 0.08

print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {inss_empregador:.2f}")
print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {inss_empregado:.2f}") 
