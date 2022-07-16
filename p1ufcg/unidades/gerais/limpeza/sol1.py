if __name__ == "__main__":
    tipo_limpeza = input()
    
    if tipo_limpeza == "1":
        
        tamanho_caixa = float(input())
        preco_final = tamanho_caixa * 80
        
        print(f"R$ {preco_final:.2f}")
        
        if preco_final >= 200:
            print("Brinde!")
    
    elif tipo_limpeza == "2":
    
        tamanho_caixa = float(input())
        preco_final = tamanho_caixa * 50
        
        print(f"R$ {preco_final:.2f}")
        
        if preco_final >= 200:
            print("Brinde!")
    
    elif tipo_limpeza == "3":

        print("R$ 50.00")

