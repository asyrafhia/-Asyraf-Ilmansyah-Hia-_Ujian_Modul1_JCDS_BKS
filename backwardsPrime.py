def backwardsPrime(start, stop):

    def prime_num(num):    
        prime_tab = []
        for i in range(2,num+1):
            if num % i == 0:
                prime_tab.append(True)
        if sum(prime_tab) == 1:
            return True
        else:
            return False 
    check_prime = []
    backward_prime = []
    
    for prime in range(start, stop+1):
        if prime_num(prime):
            check_prime.append(prime)        

    for j in check_prime:
        if prime_num(int(str(j)[::-1])) and j > 11:
            backward_prime.append(j)

    return backward_prime        

print(backwardsPrime(2,100))
print(backwardsPrime(9900,10000))
print(backwardsPrime(501,599))