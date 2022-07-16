if __name__ == "__main__":
    nota1_aluno1 = float(input())
    nota2_aluno1 = float(input())
    nota3_aluno1 = float(input())
    idade_aluno1 = int(input())

    nota_aluno1 = 0.3 * nota1_aluno1 + 0.4 * nota2_aluno1 + 0.3 * nota3_aluno1
    
    nota1_aluno2 = float(input())
    nota2_aluno2 = float(input())
    nota3_aluno2 = float(input())
    idade_aluno2 = int(input())

    nota_aluno2 = 0.3 * nota1_aluno2 + 0.4 * nota2_aluno2 + 0.3 * nota3_aluno2


    if nota_aluno1 > nota_aluno2:
        print(f"O primeiro candidato foi aprovado com média {nota_aluno1:.1f}.")
    elif nota_aluno1 < nota_aluno2:
        print(f"O segundo candidato foi aprovado com média {nota_aluno2:.1f}.")
    else:
        if idade_aluno1 > idade_aluno2:
            print(f"O primeiro candidato foi aprovado com média {nota_aluno1:.1f}.")
        elif idade_aluno1 < idade_aluno2:
            print(f"O segundo candidato foi aprovado com média {nota_aluno2:.1f}.")
        else:
            print("Empate.")



