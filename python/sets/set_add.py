nums = int(raw_input())
stamps = set()
#iterate over raw_input
for x in range(nums):
    #put stamps in set
    stamps.add(raw_input())
#get length of unique
print len(stamps)