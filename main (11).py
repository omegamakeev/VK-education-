#coding: utf-8
def print_unique_chars():
    s = input().lower()
    unique_chars = set()
    for c in s: 
        if c != ' ': 
            unique_chars.add(c)
    result = sorted(unique_chars)
    result_str = ' '.join(map(str, result))
    print(result_str)
print_unique_chars()
