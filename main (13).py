#coding: utf-8
import re 
def print_valid_words(): 
    text = input()
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words: 
        if word in word_count: 
            word_count[word] += 1 
        else: 
            word_count[word] = 1 
    valid_words = []
    for word, count in word_count.items():
        if len(word) >= 5 and len(set(word)) >= 4 and count > 2:
            valid_words.append(word)
    valid_words.sort()
    print(' '.join(valid_words))
print_valid_words()