import random
hidden_num = random.randint(1,100)
guessed_num = ''

while guessed_num != hidden_num:
    guessed_num = int(input("Enter a number: "))
    
    if guessed_num > hidden_num:
        print("Lower!")
    elif guessed_num < hidden_num:
        print("Higher!")
    else:
        print("You guessed the correct answer!")
        break