from random import randint

n = int(input("Enter length array: "))
b = 0

l = [randint(1, 10) for i in range(n)]
print(l)

t = int(input("Enter the number you want to find: "))

for i in l:
    if t == i:
        b += 1
print(t, b)
