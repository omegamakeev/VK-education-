grani = int(input())
grani1 = int(input())
otvet = False
while num := input():
    if int(num) in range(grani, grani1+1):
        otvet = True
    else:
        otvet = False
print(otvet)