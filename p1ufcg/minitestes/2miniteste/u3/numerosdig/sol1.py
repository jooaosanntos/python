num1 = int(input())
num2 = int(input())
num3 = int(input())

ctt = 0

if num1 == num2:
    ctt += 2
    if num1 == num3:
        ctt += 1
elif num2 == num3:
    ctt += 2
elif num3 == num1:
    ctt += 2

print(ctt)
