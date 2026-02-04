import random
emojis = {'r':'🪨', 's': ' ✂️', 'p':'📜'} # emojis for the better visuals
choice = ('r', 'p', 's')

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s):") # taking user inputs
    if user_choice not in choice: # its for the invalid inputs
        print("invalid input")
        continue 
    
    """ this will start the program from the begining after promiting invalid if not present it goes to line 13 and pops error by saying error on line 13 
     because we gave emoji-user choice there's nothing specified for the invalid inputs
       to tackle with it we use continue
         because we gave the space it will execute the rest of the code and gets the error in btw.  """
    
    computer_choice = random.choice(choice) # letting the program choose a random variable

    print(f"You choose {emojis[user_choice]}")
    print(f"The computer choose {emojis[computer_choice]}")

    if user_choice == computer_choice: # when both choose the same choice
        print("It's a Tie")
    elif ( 
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p' and computer_choice == 'r') or 
    (user_choice == 'r' and computer_choice == 's') ) : # for multiline conditions we are using ()
        print("You win!")
    else:
        print("You loose!")

    should_continue = input("Do you want to continue? (y/n):") # asking if the user wants to still continue the play
    if should_continue == 'n':
        print("Thanks For Playing")
        break