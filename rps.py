import random 

options = ["rock","paper","scissors"] 
computer_wins = 0
user_wins = 0 


while True:
    user = input("Enter Rock/Paper/Scissors or q to quit the game: ").lower() 
    if user == 'q':
        break
    elif user not in options:
        continue 
    
    random_number = random.randint(0,2) 
    computer_pick = options[random_number]
    print(computer_pick) 

    if user == "rock" and computer_pick == "scissors":
        user_wins += 1
    elif user == "paper" and computer_pick == "rock":
        user_wins += 1
    elif user == "scissors" and computer_pick == "paper":
        user_wins += 1

    else:
        computer_wins += 1

        
print("Goodbye")
print(f"Computer scored {computer_wins} ")
print(f"User scored {user_wins}")
if computer_wins > user_wins:
    print("Computer have won !")
else:
    print("You have won !") 



# Lessons learned
# understood the continue and break statement with vivid clarity.
# merely got some flow of the program 