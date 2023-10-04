# Prime Happy

"""
A number n is called prime happy if there is at least one prime less than n and the sum of all primes less than n is evenly divisible by n. Write isPrimeHappy(n) which returns true if n is prime happy else false.

"""


# My Solution

def is_prime_happy(n):
    prime_list = []
    for i in range(0, n):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    
    return True if prime_list and sum(prime_list) % n == 0 else False
    

# Other Solutions

from gmpy2 import next_prime
def is_prime_happy(n):
    a = 2
    r = []
    while a<n:
        r += [a]
        a = next_prime(a)
    return len(r)>1 and sum(r)%n==0