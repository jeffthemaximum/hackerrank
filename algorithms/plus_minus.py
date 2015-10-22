
from __future__ import division
import pudb

line1 = "6"
line2 = "-4 3 -9 0 4 1"

#make line1 an int
line1 = int(line1)
#make line2 an array of ints
line2 = [int(x) for x in line2.split(" ")]
total_neg = 0
total_pos = 0
total_zero = 0
total_nums = line1

#pu.db

for x in line2:
    if x < 0:
        total_neg += 1
    elif x > 0:
        total_pos += 1
    else:
        total_zero += 1

pos = total_pos / total_nums
neg = total_neg / total_nums
zero = total_zero / total_nums

print '%.3f' % pos
print '%.3f' % neg
print '%.3f' % zero
