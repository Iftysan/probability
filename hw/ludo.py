import random

dice = random.randint(1, 6)

print("Rolling the dice...")

if dice == 6:
    print("You got a 6!")
    print("The game can be started!")
else:
    print("You did not get a 6.")
    print("Roll again!")

probability = 1 / 6

print("The probability of getting a 6 is:", probability)