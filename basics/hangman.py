import random

word_list = ['ardvark', 'baboon', 'camel']
word = random.choice(word_list)
riddle = list(len(word) * '_')
print(*riddle, sep='')

while '_' in riddle:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for index in range(len(word)):
            letter = word[index]
            if letter == guess:
                riddle[index] = letter
            else:
                continue
    print(*riddle, sep='')
