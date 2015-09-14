len1 = input()
list1 = [int(i) for i in raw_input().split()]
len2 = input()
list2 = [int(i) for i in raw_input().split()]
unique_set = set(list1) ^ set(list2)
for i in sorted(unique_set):
    print i
