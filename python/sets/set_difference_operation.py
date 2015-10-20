line1 = "9"
line2 = "1 2 3 4 5 6 7 8 9"
line3 = "9"
line4 = "10 1 2 3 11 21 55 6 8"

line2 = line2.split(" ")
line4 = line4.split(" ")
set2 = set([int(x) for x in line2])
set4 = set([int(y) for y in line4])

ret = set2.difference(set4)
print len(ret)