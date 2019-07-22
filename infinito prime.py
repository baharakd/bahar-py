
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

prime = open("prime.txt", mode="w+", encoding="utf-8")
for i in get_primes(45):
    print(i)
    prime_txt = str(i)+"\n"
    prime.write(prime_txt)
