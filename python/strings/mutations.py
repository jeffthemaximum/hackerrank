line = raw_input()
data = raw_input().split()
char_to_insert = data[1]
index_for_char = int(data[0])
print line[:index_for_char] + char_to_insert + line[(index_for_char+1):]