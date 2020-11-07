
def rowSumOddNumbers(x):
    n = 1
    sum = 0
    for i in range(x):
        for j in range(x-i-1):
            print(' ', end='*')
        for j in range(i+1):
            # if n > 100:
            #     print(' ',n,end='')
            if n>10:
                print(' ',n,end='')                
            else:
                print(' ',n,end='*')  # end untuk tetap pada baris yang sama
            
            if i == (x-1):
                sum += n

            n += 2
        print('')  # atau print() untuk enter
    print(f'Jumlah angka-angka di line terakhir adalah {sum}')
        
rowSumOddNumbers(5)


# rowSumOddNumbers(1)
rowSumOddNumbers(2)
rowSumOddNumbers(10)