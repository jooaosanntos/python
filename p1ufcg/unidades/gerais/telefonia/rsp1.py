tempo = int(input())

valor = 1

if tempo < 4:
    valor += (tempo / 2)
elif tempo > 3:
    blocos = tempo // 5
    resto_blocos = tempo % 5

    if resto_blocos == 0:
        valor += (blocos * 3)
    else:
        valor += (blocos * 3 + resto_blocos * 0.7)

print(f"R$ {valor:.2f}")
