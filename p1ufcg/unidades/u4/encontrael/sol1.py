num = int(input())
list_num = input().split(" ")

rsp = "não"

for i in range(len(list_num)):
    list_num[i] = int(list_num[i])
    if list_num[i] == num:
        rsp = "sim"
        break

print(rsp)
