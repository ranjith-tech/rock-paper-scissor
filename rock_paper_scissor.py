import random
def play():
    quit = False
    while not quit:
        print("0 - to exit game: ")
        choice = input("Enter your choice: \n").lower()
        if(choice == "0"):
            break
        print("your choice is, " , choice)
        choices = ["rock", "paper", "scissor"]
        cpu_choice = random.choice(choices)
        if(choice == "rock" or choice == "paper" or choice == "scissor"):
            if(choice == cpu_choice):
                print("it's is a tie")
            elif(choice == 'rock' and cpu_choice == "scissor"):
                print("you win")
             
            elif(choice == "scissor" and cpu_choice == "paper"):
                print("you win")
              
            elif(choice == "paper" and cpu_choice == "rock"):
                print("you win")
              
            else:
                print("enemy win")
              
        else:
            print("enter the choice rock, paper, scissor.")
    


if __name__ == "__main__":
    play()