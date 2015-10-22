line1 = int(raw_input())
matrix = []

for i in range(line1):
    line = raw_input().split(" ")
    matrix.append([int(x) for x in line])

sum1 = 0

#sum1
for i in range(line1):
    sum1 += matrix[i][i]

sum2 = 0

#sum2
for i in range(line1):
    sum2 += matrix[i][(line1 - 1) - i]

dif = abs(sum1 - sum2)
print dif