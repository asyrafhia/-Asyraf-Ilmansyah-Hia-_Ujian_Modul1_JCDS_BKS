def hollowTriangle(x):
    if x == 1:
        print('#')
    else:
        atas = ['_'*(x-1) + '#' + '_'*(x-1)]
        bawah = ['#'*((2*x)-1)]  #3a+b=5  #2a+b=3  #2x-1=y
        tengah = []
        for i in range(x-2, 0, -1): #2a+b=0  #3a+b=1  #x-2=y
            tengah.append('_'*i + '#' + ('_'*(((2*x)-3)-2*i)) + '#' + '_'*i)  #2x-5=y  #2x-3-2

        print(atas[0])
        for i in tengah:
            print(i)
        print(bawah[0])

hollowTriangle(1)
print('\n')
hollowTriangle(2)
print('\n')
hollowTriangle(3)
print('\n')
hollowTriangle(4)
print('\n')
hollowTriangle(5)
print('\n')
hollowTriangle(6)
print('\n')
hollowTriangle(7)
