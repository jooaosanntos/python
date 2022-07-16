def eh_roteiro(iata, voos, roteiro):
    lista_roteiro = roteiro.split("/")

    for indice_cidade in range(len(lista_roteiro) - 1):
        
        iata_cidade1 = iata[lista_roteiro[indice_cidade]] 
        iata_cidade2 = iata[lista_roteiro[indice_cidade + 1]]
        
        voos_diretos = voos[iata_cidade1]
        
        eh_possivel = False
        for voo_direto in voos_diretos:
            
            if voo_direto == iata_cidade2:
                eh_possivel = True
                break
        if not eh_possivel: return False

    return True


