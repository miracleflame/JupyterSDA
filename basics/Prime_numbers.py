def primes_up_to(n):
    for x in range(0, n):
        for y in range(2, x):
            if x % y == 0:
                print(f"{x} = {y}*{x//y}")
                break

        else:
            # loop fell through without finding a factor
            print(x, 'is a prime number')

primes_up_to(100)

###
# primes = [2, 3, 5, 7, 11, 13, 17]
#
# def get_prime_factors(n: int):
#     factors = []
#     for prime in primes:
#         while n % prime != 0:
#             factors.append(prime)
#     return factors
#
# print(get_prime_factors(17))