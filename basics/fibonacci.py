def fibonacci(x=None):
    condition = "A number higher than 2 has to be entered to get actual fibonacci sequence!"
    n1 = 0
    n2 = 1
    if not x:
        x = input('How many numbers do you wish to generate in fibonacci sequence?: ')
    try:
        x = int(x)
    except ValueError:
        print(condition)
        return
    if x <= 2:
        print(condition)
    else:
        print(n1)
        print(n2)
        while x > (x - (x - 2)):
            n3 = n1 + n2
            print(n3)
            n1 = n2
            n2 = n3
            x -= 1

def fibonacci_recursive(x):
    if x == 1 or x == 0:
        return x
    else:
        x = (fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2))
        return x

n = 500
for i in range(0,n+1):
    print(fibonacci_recursive(i))

