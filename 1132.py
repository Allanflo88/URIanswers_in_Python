a = int(input())
b = int(input())
x = 0
if a > b:
    for i in range(b, a+1):
        if i % 13 != 0:
            x = x + i
else:
    for i in range(a, b+1):
        if i % 13 != 0:
            x = x + i

print(x)
