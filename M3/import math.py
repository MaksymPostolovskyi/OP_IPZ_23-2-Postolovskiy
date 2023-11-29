import  math

file = open ('Untitled-1', 'r')
a = file.read().split(" ")
b = list(map(float,a))
print(a)
print(b)
c = list()
for i in range(len(a)):
    temp = float(a[i])
    c.append(temp)
print(c)


c[1] = c[2] + c[3]
c[2] = c[1] - c[2]
out_text = list(map(str, c))
f = open
print(c)

