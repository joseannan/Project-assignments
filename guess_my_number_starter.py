import random #used to generate random numbers

#ask user his name
name=input("What is your name?")
print("Hi! " + name)
print("Welcome to my number guessing game!!" 
      " Think of a number between 10 and 99") #introducing the game to the user
while True:
    user_input=int(input("Guess the number:")) #ask user for his guess on the random number
    rand_num = random.randint(10,99) #generate random numbers between 10 and 99
       #condition testing
    if user_input < rand_num:
        print("You guessed too low") #output if user_input is more than the random number
    elif user_input > rand_num:
        print("You guessed too high") #output if user_input is less than the random number
    else :
        print("Congratulations! you did it!") #output if user_input is equal to rand_num
        break #exit loop after the correct number is given



