'''
Потрібно порахувати суму чисел від a до b. 
Програма запитує два числа і виводить результат - одне число.


TODO input:
2
4
TODO output:
9
'''

a = int(input("TODO input:\n"))
b = int(input())


total = 0


for i in range(a, b + 1):
    total += i


print("TODO output:")
print(total)
