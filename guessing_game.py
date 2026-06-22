import random

number = random.randint(1,100)
guess = 0 

while guess != number:
    guess = int(input("Enter a number between 1 and 100:"))
    
if guess > number:
    print("Too! high try low!")
elif guess< number:
    print("Too! low try high!")
else:
    print("yeah! that's the answer")
