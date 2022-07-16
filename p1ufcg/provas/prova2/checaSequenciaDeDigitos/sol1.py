# coding: utf-8
# PROG1 - UFCG
# ALUNO: João Pedro Juvino dos Santos | DATA : 21/03/2022 | MATRÍCULA: 121110319
# EXERCÍCIO: Checa Sequência de Dígitos

# |ENTRADA(S)|

sequencia_digitos = input()
valor_limite = int(input())

# |PROCESSAMENTO|

def eh_impar(valor):
    return valor % 2 != 0


soma_digitos = 0
numeros_lidos = 0
quantidade_impares = 0
caso = 0
quantidade_numeros = len(sequencia_digitos)

indice = 0
while True:
    
    digito_atual = int(sequencia_digitos[indice])
    numeros_lidos += 1
    soma_digitos += digito_atual
    if eh_impar(digito_atual): quantidade_impares += 1    

    # Caso 1
    if quantidade_impares == 6: 
        caso = 1
        break

    # Caso 2
    if soma_digitos >= valor_limite: 
        caso = 2
        break

    indice += 1
    # Caso 3
    if indice == len(sequencia_digitos):
        caso = 3
        break

# |SAÍDA(S)|

print(f"soma: {soma_digitos}")
print(f"números lidos: {numeros_lidos} de {quantidade_numeros}")

if caso == 1:
    print("critério de parada: 6 ímpares")
elif caso == 2:
    print("critério de parada: limite")
elif caso == 3:
    print("critério de parada: final da sequência")

