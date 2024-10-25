a = bytes([0,1,2]) # type : byte string

print(type(a))

b = bin(a[2])

print(f"b : {b}")

print(type(b))

c = a[0]

print(type(c))

d = bytearray([0,1,2])

print(type(d))

e = d[0]

print(type(e))