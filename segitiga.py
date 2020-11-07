# Segitiga atas kanan dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = 0
while(a<=var_inp):
    if a > 0:
        print(" * " * a)
    a += 1 """

# Segitiga bawah kanan dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
b = var_inp
while(b>=0):
    if b > 0:
        print(" * " * b)
    b -= 1 """

# Segitiga atas kiri dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = var_inp
b = 0
while(a>=0):
    if b > 0:
        print("   " * a + " * " * b )
    a -= 1
    b += 1 """

# Segitiga bawah kiri dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = 0
b = var_inp
while(a<=var_inp):
    if b > 0:
        print("   " * a + ' * ' * b)
    a += 1
    b -= 1 """

# Segitiga kiri dan kanan atas dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = var_inp
b = 0
c = 0
while(a>=0):
    if b > 0:
        print("   " * a + " * " * b + " * " * c)
    a -= 1
    b += 1
    if b == 1:
        c = 0
    else:
        c += 1 """

# Segitiga kiri dan kanan bawah dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = 0
b = var_inp
c = var_inp - 1
while(a<=var_inp):
    if b > 0:
        print("   " * a + " * " * b + " * " * c)
    a += 1
    b -= 1
    if b == 1:
        c = 0
    else:
        c -= 1 """

# Segitiga atas dan bawah kanan dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = 0
while(a<=var_inp):
    if a > 0:
        print(" * " * a)
    a += 1

b = var_inp-1
while(b>=0):
    if b > 0:
        print(" * " * b)
    b -= 1 """

# Segitiga atas dan bawah kiri dari sebuah Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = var_inp
b = 0
while(a>=0):
    if b > 0:
        print("   " * a + " * " * b)
    a -= 1
    b += 1

a = 0
b = var_inp
while(a<=var_inp-1):
    if a > 0:
        print("   " * a + " * " * b)
    a += 1
    b -= 1 """


# Segitiga Belah Ketupat
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = var_inp
b = 0
c = 0
while(a>=0):
    if b > 0:
        print("   " * a + " * " * b + " * " * c)
    a -= 1
    b += 1
    if b == 1:
        c = 0
    else:
        c += 1

a = 1
b = var_inp - 1
c = var_inp - 2
while(a<=var_inp):
    if b > 0:
        print("   " * a + " * " * b + " * " * c)
    a += 1
    b -= 1
    if b == 1:
        c = 0
    else:
        c -= 1 """


# Jam Pasir
""" var_inp = int(input('Masukkan angka jumlah bintang segitiga: '))
a = 0
b = var_inp
c = var_inp - 1
while(a<=var_inp):
    if b > 0:
        print("   " * a + " * " * b + " * " * c)
    a += 1
    b -= 1
    if b == 1:
        c = 0
    else:
        c -= 1

a = var_inp - 2
b = 2
c = 1
while(c<=var_inp-1):
    # if a > 0:
    print("   " * a + " * " * b + " * " * c)
    a -= 1
    b += 1
    c += 1 """