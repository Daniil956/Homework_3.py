n = int(input("Enter length array: "))
i = list(range(1,n+1))
print(i)

t = int(input("Enter the number you want to find: "))
u = int(1)

for x in i:
    if x == t:
        print(x)
if n < t:
    print(n)
if t < u:
    print(u)
