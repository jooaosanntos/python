from time import time
from os import system
from playsound import playsound

def temporizar(tempo_inicial, quantidade_de_segundos):
    print("CRONÔMETRO RODANDO...")
    anterior = 0
    while True:
        tempo_atual = int(time())
        
        if quantidade_de_segundos == (tempo_atual - tempo_inicial):
            print("Acabou o tempo!")
            playsound("alarme.mp3")
            break
        tempo_passado = tempo_atual - tempo_inicial
        if tempo_passado % 1 == 0 and tempo_passado != anterior:
            system("clear")
            print("CRONÔMETRO RODANDO")
            print("=" * 40)
            print(f"{tempo_passado} segundos passados")
            print("=" * 40)
            anterior = tempo_passado

    return 0

print("Digite o tempo em minutos: ")
qtd_horas = int(input())
qtd_segundos = qtd_horas * 60

tempo_do_inicio = int(time())
temporizar(tempo_do_inicio, qtd_segundos)
