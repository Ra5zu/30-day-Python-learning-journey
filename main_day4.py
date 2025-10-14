import random

a = random.randint(1,100)

b = 0
while a != b:
    b = int(input("Guess the number (range 1-100):"))
    if a > b:
        print("Guess higher")
    if b > a:
        print("Guess lower")
print(f"You got it! The number was {a}")