def mais_consoantes(palavra):
    qtd_vogais = 0
    qtd_consoantes = 0
    for caractere in palavra:
        if caractere.lower() in "aeiou":
            qtd_vogais += 1
        else:
            qtd_consoantes += 1
    
    return qtd_consoantes > qtd_vogais

qtd_de_palavras = 0
while True:
    palavra = input()
    qtd_de_palavras += 1
    
    tem_mais_consoantes = mais_consoantes(palavra)
    if tem_mais_consoantes: break

print(qtd_de_palavras)
