import random

# For win score....
comp_wins = 0
player_wins = 0

print("          ROCK,  PAPER,  SCISSOR          ")
print("")
print("Introduction.")
print("")
print("For rock choose 'R','r',''rock','ROCK'.")
print("")
print("For paper choose 'P','p','paper','PAPER'.")
print("")
print("For scissor choose 'S','s','scissor','SCISSOR'.")

# Taking user input and printing....
def Choose_Option():
    user_choice = input("Choose Rock, Paper, Scissor : ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice


# Taking computer input....
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


# Main game....
while True:
    print("")
    
    # Importing User and computer choices
    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")
    
    # Comparing and deciding who won....
    # User input rock comparing to computer INPUTS...
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. Tie.")
        
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1
            
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_wins += 1

    # User input paper comparing to computer INPUTS...

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1
        
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. Tie.")
            
            
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    # User input scissors comparing to computer INPUTS...
    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1
        
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_wins += 1
            
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors.  Tie.")

    # Changing +1 from integer to string...
    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")
    
    # To ask to REPLAY...
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break


# Welcome
# Take input from user
# Generate random from rock paper scissor (Assign to computer)
# Compare user input with computer 
# Check for win
# Print the result
