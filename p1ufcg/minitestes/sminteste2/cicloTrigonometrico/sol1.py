angulo = float(input())

angulo_final = angulo % 360

if angulo_final == 0 or angulo_final == 90 or angulo_final == 180 or angulo_final == 270:
    print("Sobre eixos")
else:
    if angulo_final > 0 and angulo_final < 90:
        print("Quadrante 1")
    elif angulo_final > 90 and angulo_final < 180:
        print("Quadrante 2")
    elif angulo_final > 180 and angulo_final < 270:
        print("Quadrante 3")
    elif angulo_final > 270:
        print("Quadrante 4")
