string = input()
horario = int(input())

if string == "":
    print("Condomínio em Paz.")
elif horario <= 6 or horario >= 22:
    print("Perturbação Detectada!")
else:
    print("Condomínio em Paz.")
