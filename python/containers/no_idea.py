line1 = map(int, raw_input().split())
line2 = map(int, raw_input().split())
line3 = map(int, raw_input().split())
line4 = map(int, raw_input().split())
happiness = 0
for line2_num in line2:
    for line3_num in line3:
        if line3_num == line2_num:
            happiness += 1
    for line4_num in line4:
        if line4_num == line2_num:
            happiness -= 1
print happiness
