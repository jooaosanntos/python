def troca_case(palavra):
    nova_palavra = ""
    for elemento in palavra:

        if ord(elemento) >= 65 and ord(elemento) <= 90:
            nova_palavra += chr(ord(elemento) + 32)
        elif ord(elemento) >= 97 and ord(elemento) <= 122:
            nova_palavra += chr(ord(elemento) - 32)
        else:
            nova_palavra += elemento

    return nova_palavra

def troca_letras(palavra):
    nova_palavra = ""
    for elemento in palavra:
        
        if elemento == "a" or elemento == "A":
            nova_palavra += "4"
        elif elemento == "b" or elemento == "B":
            nova_palavra += "8"
        elif elemento == "e" or elemento == "E":
            nova_palavra += "3"
        elif elemento == "g" or elemento == "G":
            nova_palavra += "6"
        elif elemento == "i" or elemento == "I":
            nova_palavra += "1"
        elif elemento == "l" or elemento == "L":
            nova_palavra += "7"
        elif elemento == "s" or elemento == "S":
            nova_palavra += "5"
        elif elemento == "o" or elemento == "O":
            nova_palavra += "0"
        else:
            nova_palavra += elemento
    return nova_palavra

def troca_asteriscos(palavra):
    nova_palavra = ""
    palavra_anterior = ""
    for elemento in palavra: 
        if elemento == " ":
            for rep in range(len(palavra_anterior)):
                nova_palavra += "*"
            palavra_anterior = ""
        else:
            palavra_anterior += elemento
            nova_palavra += elemento
    return nova_palavra

def ofuscador(linha):
    case_alterado = troca_case(linha)
    letras_trocadas = troca_letras(case_alterado)
    sem_espacos = troca_asteriscos(letras_trocadas)

    return sem_espacos



# Meus testes
def test_1():
    assert ofuscador("Eu amo Jesus!") == "3U**4M0***j35U5!"

def test_2():
    assert ofuscador("E") == "3"

def test_3():
    assert ofuscador("abc  iii") == "48C***111"

test_1()
test_2()
test_3()
