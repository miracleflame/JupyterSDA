# Ask user how many fibonacci numbers to generate



# Function to generate fibonacci numbers
def generate(this_many):
    n = 0
    for i in range(0, this_many+1):
        n += i
        print(n)

generate(int(input("How many fibonacci numbers to generate?: ")))