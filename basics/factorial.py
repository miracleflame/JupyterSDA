# attempt #1
n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    print(fact)


# attempt #2
def factorial2(n):
    x = n
    while n > 1:
        x = x * (n - 1)
        n -= 1
    print(f"Vysledok je {x}")


factorial2(5)

# attempt #3
def factorial3(n):
    """Calculate factorial.

    Args:
        n: Natural number as input for the algorithm.
    Returns:
        factorial of number n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial3(n - 1)

print(factorial3(200))


# attempt #4
memo = {}
def factorial4(n):
    if n < 2:
        return 1
    if n not in memo:
        memo[n] = n * factorial4(n - 1)
    return memo[n]

print(factorial4(200))

