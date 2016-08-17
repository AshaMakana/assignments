def fibo(n):
    b = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        
        for i in range(2, n):
            
            b.append(my_fib(i))
        
        return b
def my_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_fib(n-1) + my_fib(n-2)
print(fibo(10))


