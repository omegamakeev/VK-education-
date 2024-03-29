#coding: utf-8
def print_most_frequent_word():
    text = input().lower()
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1 
        else:
            word_count[word] = 1 
    max_count = max(word_count.values())
    most_frequent_word = None 
    for word, count in word_count.items(): 
        if count == max_count:
            most_frequent_word = word 
            break
    print(f"{most_frequent_word} {max_count}")
print_most_frequent_word()