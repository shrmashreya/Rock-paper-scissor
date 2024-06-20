from tkinter import *
from PIL import Image,ImageTk
from random import randint



root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#114E53")
root.geometry("2000x2000")


# picture
rock_img = ImageTk.PhotoImage(Image.open("rockuser.png"))
paper_img = ImageTk.PhotoImage(Image.open("paperuser.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissoruser.png"))
rk_img = ImageTk.PhotoImage(Image.open("rockcomp.png"))
pp_img = ImageTk.PhotoImage(Image.open("papercomp.png"))
sc_img = ImageTk.PhotoImage(Image.open("scissorcomp.png"))


#insert picture
user_label = Label(root , image=rock_img , bg = "#114E53")
comp_label = Label(root , image=rk_img , bg = "#114E53")
user_label.grid(row=4 ,column=3)
comp_label.grid(row=4 ,column=9)

#spaces
space1 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=0 , column=5)
space2 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=1 , column=5)
space3 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=3 , column=5)
space4 = Label(root,text=" space" , font="50" ,bg="#114E53" , fg="#114E53").grid(row=4 , column=0)
space5 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=4 , column=1)
space6 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=4 , column=2)
space7 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=5 , column=5)
space8 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=6 , column=5)
space9 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=7 , column=5)
space10 = Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=8 , column=5)
space11= Label(root,text="space " , font="50" ,bg="#114E53" , fg="#114E53").grid(row=9 , column=5)

#scoreboard
playerScore = Label(root,text=0,font=100,bg="#114E53",fg="white")
compScore = Label(root,text=0,font=100,bg="#114E53",fg="white")
playerScore.grid(row=4 , column=4)
compScore.grid(row=4 , column=8)

#indicator
user_indicator = Label(root,text="USER" , font="50" ,bg="#114E53" , fg="white").grid(row=2 , column=4)
computer_indicator = Label(root,text="COMPUTER" , font="50" ,bg="#114E53" , fg="white").grid(row=2 , column=8)

#msg

msg = Label(root,font=50,bg="#114E53" , fg="white" , text="You Loose")
msg.grid (row=12 ,column=6)

choices = ["rock" , "paper" , "scissor"]

def updateChoice(x):
    #for computer
    comp_choice = choices[randint(0,2)]
    if (comp_choice=="rock"):
        comp_label.configure(image=rk_img)
    if (comp_choice=="paper"):
        comp_label.configure(image=pp_img)
    if (comp_choice=="scissor"):
        comp_label.configure(image=sc_img)
    #for user
    if (x=="rock"):
        user_label.configure(image=rock_img)
    if (x=="paper"):
        user_label.configure(image=paper_img)
    if (x=="scissor"):
        user_label.configure(image=scissor_img)
    checkWin(x,comp_choice )

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)

def updateCompScore():
    score = int(compScore['text'])
    score += 1
    compScore['text'] = str(score)

def checkWin(player,computer):
    if player == computer:
        updateMessage("it's a tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompScore()
        elif computer == "scissor":
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "rock":
            updateMessage("You Win")
            updateUserScore()
        elif computer == "scissor":
            updateMessage("You Loose")
            updateCompScore()
    elif player == "scissor":
        if computer == "paper":
            updateMessage("You Win")
            updateUserScore()
        elif computer == "rock":
            updateMessage("You Loose")
            updateCompScore()
    else:
        pass        

        
#buttons
rock = Button(root,text="ROCK",height=2 ,width=20 , bg="#839b45" , command= lambda:updateChoice("rock") ,fg= "white").grid(row=10 , column=5)
paper = Button(root,text="PAPER",height=2 ,width=20 , bg="#478dbe" ,command= lambda:updateChoice("paper"), fg= "white").grid(row=10 , column=6)
scissor = Button(root,text="SCISSSOR",height=2 ,width=20 , bg="#df913e" ,command= lambda:updateChoice("scissor") , fg= "white").grid(row=10 , column=7)


root.mainloop()