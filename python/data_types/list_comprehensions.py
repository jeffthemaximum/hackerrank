def possible_vals(sum):
    return range(sum+1)

x = raw_input()
y = raw_input()
z = raw_input()
n = raw_input()
xlist = possible_vals(x)
ylist = possible_vals(y)
zlist = possible_vals(z)
a = []
[a.append([d, b, c]) for d in xlist for b in ylist for c in zlist if d+b+c != n]
print a
