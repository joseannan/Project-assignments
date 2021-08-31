import random

#ask user his name
name=input("What is your name?")
print("Hi! " + name)
print("Welcome to my number guessing game!!"
      " Think of a number between 1 and 9")
while True:
    user_input=int(input("Guess the number:"))
    rand_num = random.randint(1,9)
    if user_input < rand_num:
        print("You guessed too low")
    elif user_input > rand_num:
        print("You guessed too high")
    else :
        print("Congratulations! you did it!")
        break



