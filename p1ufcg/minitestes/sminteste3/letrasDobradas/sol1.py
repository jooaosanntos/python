num_palavras = int(input())

palavras_rep = ""
num_palavras_rep = 0
palavras_notrep = ""
num_palavras_notrep = 0
letra_anterior = ""
eh_repetida = False
for n in range(num_palavras):
    palavra = input()
    for index in range(len(palavra)):
        if index == 0:
            letra_anterior = palavra[0]
            continue
        if palavra[index] == letra_anterior:
            eh_repetida = True
            break
        letra_anterior = palavra[index]

    if eh_repetida:
        palavras_rep += f"{palavra}+"
        num_palavras_rep += 1
        eh_repetida = False
    else:
        palavras_notrep += f"{palavra}+"
        num_palavras_notrep += 1

print(f"{num_palavras_rep} palavra(s) com letras dobradas:")
palavra_final_rep = ""
for char in palavras_rep:
    if char == "+":
        print(palavra_final_rep)
        palavra_final_rep = ""
        continue
    palavra_final_rep += char

print("---")
print(f"{num_palavras_notrep} palavra(s) sem letras dobradas:")
palavra_final_notrep = ""
for char in palavras_notrep:
    if char == "+":
        print(palavra_final_notrep)
        palavra_final_notrep = ""
        continue
    palavra_final_notrep += char

