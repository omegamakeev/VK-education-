s = input()
words = s.split()
avg_len = sum(len(word) for word in words) / len(words)
print(round(avg_len, 2))