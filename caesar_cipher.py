
# https://en.wikipedia.org/wiki/Caesar_cipher
# Caesar Cipher

# input = jakarta
# output = lcmctvc

var = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
var_1 = input('Masukkan: ').upper()
# var_1 = 'ASYRAF'
# print(var_1[0])
b = ''
k = 0
                              # var_1 = 'WXYZ'
for i in range(0,len(var_1)): # i = 0 1 2
    a = var.index(var_1[i]) # a = 22 23 24
    if ((a+2) < len(var)): # (a+2) = 24 25 26
        b += var[a+2]   # b = YZ
    elif ((a+2) >= len(var)):
        b += var[k]
        k += 1
print(b)