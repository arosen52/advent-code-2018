path = 'data/input_day1.txt'

dfile = open(path, 'r')
x = dfile.read()
y = x.split('\n')

ans = sum(int(i) for i in y[:-1])
print(ans)
