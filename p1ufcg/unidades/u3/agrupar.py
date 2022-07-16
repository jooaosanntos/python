num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if num1 > num2:
    num1, num2 = num2, num1
if num3 < num1:
    num1, num3 = num3, num1
if num3 < num2:
    num3, num2 = num2, num3
if num4 < num3:
    num3, num4 = num4, num3
if num3 < num2:
    num3, num2 = num2, num3
if num1 > num2:
    num1, num2 = num2, num1

print(num1, num2, num3, num4)
