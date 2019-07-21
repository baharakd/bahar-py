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
a = get_primes(3)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

