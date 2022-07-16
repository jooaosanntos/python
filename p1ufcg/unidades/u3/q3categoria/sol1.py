nome = input()
idade = int(input())

if idade > 17:
    print(f"{nome}, {idade} anos, Senior.")
elif idade > 13:
    print(f"{nome}, {idade} anos, Juvenil B.")
elif idade > 10:
    print(f"{nome}, {idade} anos, Juvenil A.")
elif idade > 7:
    print(f"{nome}, {idade} anos, Infantil B.")
elif idade > 4:
    print(f"{nome}, {idade} anos, Infantil A.")
else:
    print(f"{nome}, {idade} anos, Não pode competir.")
