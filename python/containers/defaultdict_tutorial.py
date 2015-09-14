from collections import defaultdict
import sys

line1 = raw_input().split()
n = int(line1[0])
m = int(line1[1])
d1 = defaultdict(list)
d2 = defaultdict(list)
for i in range(n):
    d1['items'].append(raw_input())
for j in range(m):
    d2['items'].append(raw_input())

for x in d2['items']:
    my_list = []
    for i in range(len(d1['items'])):
        if (d1['items'][i] == x):
            my_list.append(i+1)
    if len(my_list) == 0:
        sys.stdout.write("-1")
    else:
        for num in my_list:
            sys.stdout.write(str(num) + " ")
    sys.stdout.write("\n")
# z = 0
# for x in d2['items']:
#     count = d1['items'].count(x)
#     for k in range(count):
#         sys.stdout.write(str(d1['items'].index(x) + k + 1 + z*m) + " ")
#         d1['items'].pop(d1['items'].index(x))
#     z += 1
#     print("\n")
