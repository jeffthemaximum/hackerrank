from __future__ import division

line1 = raw_input()
line2 = raw_input()

line2 = [int(x) for x in set(line2.split(" "))]
length = len(line2)
total = sum(line2)
ret = total / length
print ret
