# from sympy import isprime
import math


def check_prime_v1(n, is_prime=None):
    """Returns is_prime=True/False and prints divisibles and statements."""
    for divisor in range(2, n):
        if n == 1:
            is_prime = False
            break
        if n % divisor == 0:
            print(f"{n} is divisible by {divisor}.")
            is_prime = False

    if is_prime == False:
        print(f"{n} is not a prime number.")
    else:
        is_prime = True
        print(f"{n} is a prime number.")
    return is_prime


def check_prime_v2(n):
    """Returns 'True' if 'n' is a prime number. False otherwise."""
    if n > 2 and n % 2 == 0 or n == 1:
        return False
    elif n == 2:
        return True

    max_divisor = math.floor(math.sqrt(n))
    for divisor in range (3, max_divisor + 1, 2):
        if n % divisor == 0:
            return False
    return True


def generate_primes_v1(n):
    """Generates a list of primes up to n and prints it out."""
    primes = []
    for x in range(2, n+1):
        for divisor in range(2, x):
            if x % divisor == 0:
                print(x, "equals", divisor, "*", x // divisor)
                break
        else:
            # loop fell through without finding a factor
            print(f"{x} is a prime number.")
            primes.append(x)
    print("Prime numbers:", primes)


def generate_primes_v2(n):
    """Generates and prints a list of primes up to n using list comprehension and a function check_prime."""
    primes = [x for x in range(2, n+1) if check_prime_v2(x)]
    print("Prime numbers:", primes)
    for prime in primes:
        print(prime)


n = int(input("Input a number for prime function: "))
# check_prime(n)
# generate_primes_v1(n)
generate_primes_v2(n)
