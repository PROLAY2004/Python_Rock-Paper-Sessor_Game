import random

def check(x):
    if(x==1):
        return "Rock"
    elif(x==2):
        return "Paper"
    elif(x==3):
        return "Scissor"
    elif(x==4):
        return False
    else:
        print("---------------------------------------------------------------")
        print("Wrong Input! Please Enter again.")
        n=int(input("Type Here : "))
        print("---------------------------------------------------------------")
        return check(n)
def again(p):
    if(p=="Y" or p=="y"):
        your_score=0
        computer_score=0
        print("---------------------------------------------------------------")
        main()
    elif(p=="N" or p=="n"):
        exit
    else:
        print("---------------------------------------------------------------")
        q=input("Wrong Input! Please Enter - Y/N :")
        return again(q)
        print("---------------------------------------------------------------")
        
def userInput():
    print("Enter your Choice :")
    print("1 : Rock")
    print("2 : Paper")
    print("3 : Scissor")
    print("4 : Exit")
    x=int(input("Type Here : "))
    return check(x)

def main():
    print("Welcome to Rock-Paper-Scissor Game.")
    choice=userInput()
    your_score=0
    computer_score=0
    dataset=["Rock","Paper","Scissor"]
    while(choice):
        i=random.choice(dataset)
        if(choice=="Rock"):
            if(i=="Scissor"):
                your_score+=1
                print("You scored! Computer choosed ,",i)
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()  
            elif(i=="Paper"):
                computer_score+=1
                print("Computer scored! Choosed ,",i)
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput() 
            else:
                print("Draw match")
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
        elif(choice=="Paper"):
            if(i=="Rock"):
                your_score+=1
                print("You scored! Computer choosed ,",i)
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
            elif(i=="Scissor"):
                computer_score+=1
                print("Computer scored! Choosed ,",i)
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
            else:
                print("Draw match")
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
        else:
            if(i=="Paper"):
                your_score+=1
                print("You scored! Computer choosed ,",i)
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
            elif(i=="Rock"):
                computer_score+=1
                print("Computer scored! Choosed ,",i)
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
            else:
                print("Draw match")
                print("Your Score : ",your_score)
                print("Computer Score : ",computer_score)
                print("---------------------------------------------------------------")
                choice=userInput()
    print("---------------------------------------------------------------")
    print("Game Ended.")
    print("Your Final Score : ",your_score)
    print("Computer's Final Score : ",computer_score)
    if(your_score>computer_score):
        print("Congratulations! You Win.")
    elif(your_score<computer_score):
        print("Computer Wins! Better Luck Next Time.")
    else:
        print("Its A Tie! Play Again To Win.")
    print("---------------------------------------------------------------")
    mindset=input("Want to play again? - Y/N : ")
    again(mindset)
main()

