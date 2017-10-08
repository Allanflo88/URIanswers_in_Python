a = {'61' : 'Brasilia', '71' : 'Salvador', '11' : 'Sao Paulo', '21' : 'Rio de Janeiro', '32' : 'Juiz de Fora', '19' : 'Campinas', '27' : 'Vitoria', '31' : 'Belo Horizonte'}
x = str(input())
x = a.get(x, -1)
if x != -1:
    print(x)
else:
    print("DDD nao cadastrado")
