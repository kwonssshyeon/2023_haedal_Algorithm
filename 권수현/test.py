a = '1101'

a = int(a,2) ^ 1<<0 ^ 1<<2
print(a)
print(bin(a))
print(type(int(bin(a)[2:])),int(bin(a)[2:]))

b = 111
