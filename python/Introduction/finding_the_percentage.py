def list_average(list):
    return sum(list)/len(list)

my_dict = {}

for i in range(0, input()):
    data = raw_input().split(" ")
    name = data.pop(0)
    data = map(float, data)
    my_dict[name] = list_average(data)

print ("{0:.2f}".format(round(my_dict[raw_input()], 2)))