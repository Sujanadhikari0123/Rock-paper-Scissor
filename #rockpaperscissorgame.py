#rock paper scissor game
import random

print("====== Rock, Paper, Scissors game ======")

choices=["rock", "paper", "scissors"]
while True:
    user = input("\nEnter rock, paper, scissors or quit to exit: ").lower()
    if user not in choices:
       print("invalied input, please try again")
       continue
    computer = random.choice(choices)
    print(f"Computer chose:", computer)

    #logic of the game
    if user == computer:
      print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or  (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
      print("You win!")
    else:
        print("you loose")
    #play again or not
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye.")

    break

    #and= both/all conditions are true ===> True else False
    # true and true ===> true
    # true and false ===> false
    # false and false ===> false
    # true and(false and true) ===> false

    #or=any condition is true ===> True 
    # true or true ===> true
    # true or false ===> true
    # false or false ===> false
    # false or (true or false) ===> true
    # false or (false or false) ===> false
    # false or (true and false) ===> false
    # False and (true or false) ===> false