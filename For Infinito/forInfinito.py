import sys

soma = 0
for linha in sys.stdin:
    if linha == "stop\n": break
    num = int(linha)
    soma += num

print(soma)
