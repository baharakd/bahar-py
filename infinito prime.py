def is_prime(num):
    for i in range(2, num):
        if num%i == 0 :
            return False
    return True


def get_primes(n):
        while True:
            if is_prime(n):
                yield n
            n += 1

for i in get_primes(15):
    print(i)


