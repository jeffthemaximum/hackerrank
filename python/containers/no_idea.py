line1 = "3 2"
line2 = "1 5 3"
line3 = "3 1"
line4 = "5 7"
line1 = map(int, line1.split())
line2 = map(int, line2.split())
line3 = map(int, line3.split())
line4 = map(int, line4.split())
happiness = 0
for line2_num in line2:
    for line3_num in line3:
        if line3_num == line2_num:
            happiness += 1
    for line4_num in line4:
        if line4_num == line2_num:
            happiness -= 1
print happiness
