line1 = "6"
line2 = "1 2 3 4 10 11"

#make line1 an int
line1 = int(line1)
#make line2 an array of ints
line2 = [int(x) for x in line2.split(" ")]
ret = sum(line2)
print ret
