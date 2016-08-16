def prime_no(n):
    if n == 0:
        return False
    elif n == 1:
        return False
    for num in range(0, n):
        for i in range(2, num):
            if num%i == 0:
                break
            else:
                return num
print(prime_no(10))
