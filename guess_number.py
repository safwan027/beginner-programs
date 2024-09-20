import random      

def guess_number():

    

    while True:
        top_of_range = input("Type an upper limit: ")
        if top_of_range.isdigit():
            top_of_range = int(top_of_range) 
            break 
        else:
            print("Please type numericals.")
            
            

    random_number = random.randint(0,top_of_range) 

    guesses = 0
    max = 5



    while True: 
        guesses += 1
        guess_number = input("Make a guess: ") 
        if guess_number.isdigit():
            guess_number = int(guess_number) 
        else:
            print("Please type numericals.")
            continue

        if guess_number == random_number:
            print(f"You got it within {guesses} tries ! ")  
            break                    
           
        elif guess_number > random_number:
            print("The guessed number is high.") 
            
        elif guess_number < random_number:
            print("The guessed number is low.")       

        

        if guesses == max:
            print(f"You have finished your maximum attempts. The number was {random_number}.")
            break    
         

guess_number() 






