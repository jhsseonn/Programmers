num = int(input())
words = {}

for _ in range(num):
    word = input()
    x = len(word)-1
    for w in word:
        if w in words:
            words[w] += 10 ** x
        else:
            words[w] = 10 ** x
        x -=1

words_sort = sorted(words.values(), reverse=True)

word_number = 9
result = 0
for i in words_sort:
    result+=i*word_number
    word_number-=1

print(result)