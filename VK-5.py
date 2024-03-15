numb1 = int(input())
numb2 = float(input())
numb3 = int(input())
numb3 = str(int(format(numb3, 'b')))
print(f"{numb1:0=+10}")
print(f"{numb2:#>10.2f}")
numb3result = f"{numb3:0>16}"
print('_'.join(numb3result[i:i+4] for i in range(0, len(numb3result), 4))[::+1])