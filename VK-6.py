text = input()
text = text.lower()
i = 0
numb = 0
while i < len(text):
  if text[i] == "@" or text[i] == "#" or text[i] == "%" or text[i] == "!":
     text = text.replace(text[i], "")
     i = 0
     numb += 1
  i += 1
print(numb)
print(text)