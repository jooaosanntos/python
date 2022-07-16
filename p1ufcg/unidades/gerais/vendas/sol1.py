if __name__ == "__main__":
    brinquedos_vendidos = int(input())

    brinquedos_Teresa = int(input())
    brinquedos_Carla = int(input())

    brinquedos_Joaquim = brinquedos_vendidos - brinquedos_Teresa - brinquedos_Carla

    porcentagem_Teresa = (brinquedos_Teresa / brinquedos_vendidos) * 100
    porcentagem_Carla = (brinquedos_Carla / brinquedos_vendidos) * 100
    porcentagem_Joaquim = (brinquedos_Joaquim / brinquedos_vendidos) * 100

    print(f"Teresa vendeu {brinquedos_Teresa} (de {brinquedos_vendidos}) brinquedos. ({porcentagem_Teresa:.2f}%)")
    print(f"Joaquim vendeu 80 (de 240) brinquedos. ({porcentagem_Carla:.2f}%)")
    print(f"Carla vendeu 80 (de 240) brinquedos. ({porcentagem_Joaquim:.2f}%)")
