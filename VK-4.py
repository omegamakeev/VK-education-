a = input()
otvet = False
if "a" in a or "o" in a:
    otvet = True
else:
    otvet = False
if "i" not in a and "e" not in a:
    otvet = True
else:
    otvet = False
print(otvet)