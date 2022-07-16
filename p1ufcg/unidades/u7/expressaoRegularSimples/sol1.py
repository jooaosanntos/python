def verificar_presenca(palavra1, palavra2, indice_comeco, indice_fim):
    palavra_final = ""
    for indice in range(indice_comeco, indice_fim):
        palavra_final += palavra1[indice]

    if palavra_final == palavra2:
        return True
    return False

def is_substring_expr(str1, str2):
    comeco, fim = str2.split("*")
    
    rsp1 = verificar_presenca(str1, comeco, 0, len(comeco))
    rsp2 = verificar_presenca(str1, fim, len(str1) - len(fim), len(str1))

    if rsp1 and rsp2:
        return True
    else:
        return False

