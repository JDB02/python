import base64

a = 'SqUGghsZwVlWAgPhvqeMBjfQ6WA='
a1 = (base64.b64decode(a)) 
a2 = (base64.b16encode(a1))


b = '5WSEkk6nNgAquTC1ji5oBLoCusw= '
b1 = (base64.b64decode(b)) 
b2 = (base64.b16encode(b1))


c = 'nmmJQ3OpruSnu+xPU5FavdKDsmU='
c1 = (base64.b64decode(c))
c2 = (base64.b16encode(c1))


d = 'CL2hZGNbWJluTx5/WbglhotvJek='
d1 = (base64.b64decode(d))
d2 = (base64.b16encode(d1))

print()
print()

print("original string")
print(a)
print(b)
print(c)
print(d)

print()
print()

print("b64 decoded string")
print(a1)
print(b1)
print(c1)
print(d1)

print()
print()

print("b16 encoded string")
print (a2)
print (b2)
print (c2)
print (d2)
