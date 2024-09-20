name =  input("Type your name: ")
print("Welcome",name,"to football emulator !") 

answer = input("You either want to be replicated in a barcelona or real madrid match ? (barca/real)").lower()

if answer == "barca":
    answer = input(f"You are here being replicated to barcelona play, Are your ready {name}? (Yes/no)").lower()
    if answer == "yes":
        pass1 = input(f"Victor valdez made a short kick pass to pique, where {name} just moved in the space to recieve the ball from pique with iniesta running upward the pitch. Are your ready to revieve the ball ?(Pass/No pass)")
    elif answer == "no":
        print("Opportunity wasted !")
    else:
        print("Type valid option.")    

    if pass1 == "pass":
        print(f"{name} just received the ball from pique and you made a beautiful pass to iniesta in the attacking third.")
    elif pass1 == "no pass":
        print("Pique misses the ball to opponents, goal is conceded and you lose.")
    else:
        print("Type valid option.") 

    pass2 = input("Does iniesta misses the ball from the pass ? (Yes/No)").lower()
    if pass2 == "yes":
        print("Show some confidence in teammates, you are ruled out !")
    elif pass2 == "no":
        print(f"Iniesta controlled ball with his magical touch and drived inside the box, meanwhile messi fell backward \n to create space so {name} sprinted to the either side of the box and raises hand for the pass.")
    else:
        print("Type valid option.") 

    pass3 = input(f"Iniesta visioned {name} move and lead a through ball.{name} have an open chance for goal or \n either pass to pedro because he yells pass? (pass/goal)").lower()

    if pass3 == "pass":
        print("ball is intecepted and misses the ball !")
    elif pass3 == "goal":
        print(f"{name} just scored a goal for barcelona, You WIN !") 
    else:
        print("Type valid option.")

elif answer == "real":
    print("Only barca fans assemble here, real madrid supporters better leave....ha ha ha")
else:
    print("Type valid option.")    


#safwan nasar