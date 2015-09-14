# First line contains N. Second line contains Array A[] of N integers each separated by a space.
line1 = raw_input()
line2 = raw_input()
my_list = sorted(list(set([int(i) for i in line2.split()])))
print my_list[len(my_list) - 2]
