def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range (2, n):
            if n > 1 :
                
                print (fibo(n-1) + fibo(n-2))
print(fibo(10))


