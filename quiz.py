def Quiz():
    playing = input("Do you want to play: ").lower() 
    if playing != "yes":
        quit() 
    
    print("Lets Start !")
    score = 0 

    
    questions_and_correct = [
        ("Under what name is the indian state Kerala known to be ? ","gods own country"),
        ("Who is termed as the GOAT of football ? ","messi"),
        ("Which car is known to be the godzilla ?","nissan gtr"),
        ("Name the famous toyota engine ?","2-jz"),
    ]

    for questions, correct in questions_and_correct:
        answer = input(questions).strip().lower() 
        if answer == correct.strip().lower():    
            print("Correct !")
            score += 1
        else:
            print("Incorrect ! The correct answer is " + correct) 
        


   
    if score > 2:
        print("Congragulations ! You gained " + str(score) + " questions right !")
        print("Your percentage is " + str((score/4)*100) +' %') 
    else:
        print("Better luck next time! You only got " + str(score) + " questions right !")
        print("Your percentage is " + str((score/4)*100) +' %') 

Quiz()   
