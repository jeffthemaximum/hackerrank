# You are given an integer N in one line. The next line contains N space-separated integers. Create a tuple of those N integers. Lets call it T.
# Compute hash(T) and print it.
line1 = raw_input()
line2 = raw_input()
int_list = [int(i) for i in line2.split()]
my_tuple = tuple(int_list)
print hash(my_tuple)
