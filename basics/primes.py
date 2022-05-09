# from sympy import isprime

def check_prime(n, is_prime=None):
    """Returns is_prime=True/False and prints divisibles and statements."""
    for divisor in range(2, n):
        if n % divisor == 0:
            print(f"{n} is divisible by {divisor}.")
            is_prime = False

    if is_prime == False:
        print(f"{n} is not a prime number.")
    else:
        is_prime = True
        print(f"{n} is a prime number.")
    return is_prime


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
    primes = [x for x in range(2, n+1) if check_prime(x)]
    print("Prime numbers:", primes)


n = int(input("Input a number for prime function: "))
# check_prime(n)
# generate_primes_v1(n)
generate_primes_v2(n)
