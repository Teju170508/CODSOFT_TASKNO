import random

while True:
    print("\n,====Rock-Paper-scissors====")
    choices=["rock","paper","scissors"]

    computer=random.choice(choices)

    player=input("Enter rock,paper or scissors:").lower()

    if player not in choices:
       print("Invalid Choice,Try Again!")
       continue

    print("computer choose:",computer)

    if player==computer:
       print("It's a tie!")
    
    elif (player=="rock" and computer=="scissors")or(player=="paper" and computer=="rock")or(player=="scissors"and computer=="paper"):
       print("Congratulations! you won!")
    elif player in choices:    
       print("computer wins!")
    else:
       print("Invalid choice!please enter Rock,Paper,Scissors.")
    play_again=input("Do you want to play again?(yes/no):").lower()
    if play_again != "yes":
       print("Thankyou for playing!")
       break
    

    
