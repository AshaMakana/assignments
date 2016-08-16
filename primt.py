def prime_no(n):
    if n==1:
        return False
    
    for i in range(1, n):
        
        if(n%i== 0):
            prime=False
        else:
            print(n)
print(prime_no(10))


