import sys

n = int(raw_input())
word_list = []
word_count = {}
repeat_count = 0

for i in range(0, n):
    word = raw_input()
    if word in word_count:
        word_count[word] += 1
    else:
        repeat_count += 1
        word_list.append(word)
        word_count[word] = 1

print repeat_count
for word in word_list:
    sys.stdout.write(str(word_count[word]) + " ")
