from fractions import Fraction

def encontrar_divisores(valor):
    valor_positivo = abs(valor)
    lista_divisores = []
    for numero in range(1, valor_positivo + 1):
        if valor_positivo % numero == 0:
            lista_divisores.append(numero)

    return lista_divisores


def adcionar_opostos(lista_valores):
    for indice in range(len(lista_valores)):
        lista_valores.append(-1 * lista_valores[indice])
    return lista_valores


def gerar_fracoes(lista1, lista2):
    lista_fracoes = []
    for elemento1 in lista1:
        for elemento2 in lista2:
            fracao = Fraction(elemento1 / elemento2)
            lista_fracoes.append(fracao)
    return lista_fracoes


def encontrar_raizes(expressao, valores):
    raizes = []
    for elemento in valores:
        resultado = eval(expressao.replace("x", f"{elemento}"))
        if resultado == 0:
            raizes.append(elemento)
    return raizes


def encontrar_an(expressao):
    an = ""
    for elemento in expressao:
        if elemento == " ": break
        an += elemento
    an = int(an)
    return an


def encontrar_a0(expressao):
    a0 = ""
    for indice in range(len(expressao) - 1, -1, -1):
        if expressao[indice] == " ": break
        a0 += expressao[indice]
    if len(a0) > 1:
        a0 = int(f"{a0[-1]}{a0[0]}")
    else:
        a0 = int(a0)
    return a0


if __name__ == "__main__":

    print("+" * 100)
    print("\nEncontra Raízes Racionais de um Polinômio!!!\n")
    print("Digite um polinômio no formato:\n\n2 * x ** 6 - 5 * x ** 5 + 4  * x ** 4 -  5 * x ** 3 - 10 * x ** 2 + 30 * x - 12\n")
    print("-" * 100)

    expressao = input("Polinômio? ")

    a0 = encontrar_a0(expressao)
    an = encontrar_an(expressao)

    divisores_a0 = encontrar_divisores(a0)
    divisores_an = encontrar_divisores(an)

    adcionar_opostos(divisores_a0)

    fracoes_set = set(gerar_fracoes(divisores_a0, divisores_an))

    raizes = encontrar_raizes(expressao, fracoes_set)


    print("\nRAÍZES\n")
    for indice in range(len(raizes)):
        print(f"Raíz {indice + 1}: {raizes[indice]}")

