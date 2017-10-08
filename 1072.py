inp = 0
out = 0
casos = int(input())
while(casos > 0):
    num = int(input())
    if(num >= 10 and num <= 20):
        inp += 1
    else:
        out += 1
    casos -= 1
print(str(inp) + " in")
print(str(out) + " out")
