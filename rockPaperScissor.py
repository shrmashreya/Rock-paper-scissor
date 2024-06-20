import random 

# Rock
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images = [Rock , Paper , Scissor]

while(True):
    userInput = int(input("enter 0 for Rock , 1 for PAper and 2 for Scissor : "))
    print("user's input is : " )
    print(game_images[userInput])
    computerChoice = random.randint(0,2)
    print("computer choice is : " )
    print(game_images[computerChoice])


    if (userInput>2 or userInput<0):
       print("invalid input so you lose")

    elif (computerChoice==userInput):
       print("match draw")   

    elif (userInput == 0 and computerChoice== 2):
       print("you win")    

    elif (userInput == 2 and computerChoice== 0):
       print("you loose") 

    elif (computerChoice>userInput):
       print("you loose")         

    elif (computerChoice<userInput):
       print("you win")


