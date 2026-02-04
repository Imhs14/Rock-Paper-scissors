import random
emojis = {'r':'🪨', 's': ' ✂️', 'p':'📜'}
choice = ('r', 'p', 's')

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s):")
    if user_choice not in choice:
        print("invalid input")
        continue
    computer_choice = random.choice(choice)

    print(f"You choose {emojis[user_choice]}")
    print(f"The computer choose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a Tie")
    elif (
    (user_choice == 's' and computer_choice == 'p') or 
    (user_choice == 'p' and computer_choice == 'r') or 
    (user_choice == 'r' and computer_choice == 's') ) :
        print("You win!")
    else:
        print("You loose!")

    should_continue = input("Do you want to continue? (y/n):")
    if should_continue == 'n':
        print("Thanks For Playing")
        break