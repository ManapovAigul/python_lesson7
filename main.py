d = {}

d[float('nan')] = 1
d[float('nan')] = 2
d[1.0] = 'float'
d[1] = 'int'
d[True] = 'bool'
print(d)