import random

options = ("ROCK", "PAPER", "SCISSOR")
gameRunning = True


player = None
computer = None
attempts = 0
player_score = 0
comp_score = 0

print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎")
print("-------------------------ROCK-PAPER-SCISSORS-------------------- ")
print("😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎\n")
print("ENJOY :)\n🪨 📃 ✂️\n")

while gameRunning:
    attempts = int(input("Of how many points do you wish the game to be??"))

    while player_score < attempts and comp_score < attempts:
        player = input("\nEnter choice:").upper()
        if player not in options:
            print("Invalid choice, try again.")
            continue

        computer = random.choice(options)
        print(f"Computer's choice:{computer}\n")
        
        if player == computer:
           print("Tie! No one gets the points")
        elif (player == "SCISSOR" and computer == "PAPER") or \
             (player == "PAPER" and computer == "ROCK") or \
             (player == "ROCK" and computer == "SCISSOR"):
            player_score += 1
            print(f"You got a point! \nYou:{player_score}/{attempts}\nComputer:{comp_score}/{attempts}")
        else:
            comp_score += 1 
            print(f"Computer got a point! \nYou:{player_score}/{attempts}\nComputer:{comp_score}/{attempts}")  
    
    
    if player_score > comp_score:
        print("CONGRATS! YOU WON 💯💯💯✨✨✨")       
    else:
        print("You LOST. Better luck next time! 🚫🚫🚫") 
    
    player_score = 0
    comp_score = 0

    regame_choice = input("Do you wish to play again?(Y/N)").upper()
    if regame_choice == "Y":
        gameRunning = True 
    else:
        gameRunning = False 
