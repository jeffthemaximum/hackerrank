line1 = raw_input()
line2 = raw_input()
len1 = len(line1)
len2 = len(line2)
counter = 0
for i in range(len1):
    if line1[i:(i+(len2))] == line2:
        counter += 1
print counter
