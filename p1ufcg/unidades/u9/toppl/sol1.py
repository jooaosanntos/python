def verificar_inscricao(matricula, lista_inscritos):
    for indice in range(len(lista_inscritos)):
        if matricula == lista_inscritos[indice]: return True
    return False

def filtra_alunos(alunos, inscritos, nota):
    contador_eliminados = 0
    for indice in range(len(alunos) - 1, -1, -1):

        esta_inscrito = verificar_inscricao(alunos[indice][0], inscritos) 
        if (not esta_inscrito or alunos[indice][1] <= nota):
            alunos.pop(indice)
            contador_eliminados += 1

    return contador_eliminados


