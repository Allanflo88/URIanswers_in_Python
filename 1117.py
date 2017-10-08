valida = 1
b = 0.0
while valida <= 2:
    a = float(input())
    if a >= 0.00 and a <=10.00:
        b = b + a
        valida += 1
    else:
        print("nota invalida")
b = b / (valida - 1)
print('media = %2.2f' % b)
