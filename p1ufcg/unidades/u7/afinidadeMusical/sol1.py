def tem_afinidade(l1, l2):
    qtd_match = 0
    for elemento1 in l1:
        for elemento2 in l2:
            if elemento1 == elemento2:
                qtd_match += 1
                break
        if qtd_match == 3: return True
    
    return False

