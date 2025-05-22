primeList = []

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True


def prime_generator(x, y):
    for num in range(x, y+1):
        if is_prime(num):
            primeList.append(num)
                    


prime_generator(0, 13)
print(primeList)
