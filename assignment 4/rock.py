import random
from tkinter import *

playerwins = 0
computerwins = 0

def Rock():
    randompick = ['rock', 'paper', 'scissors']
    computer = (random.choice(randompick))

    if computer == "rock":
        var.set("Computer selected " + computer)
        var2.set("Draw!")

    elif computer == "scissors":
        var.set("Computer selected " + computer)
        var2.set("Win!")

    elif computer == "paper":
        var.set("Computer selected " + computer)
        var2.set("Lose!")

def Paper():
    randompick = ['rock', 'paper', 'scissors']
    computer = (random.choice(randompick))

    if computer == "paper":
        var.set("Computer selected " + computer)
        var2.set("Draw!")

    elif computer == "rock":
        var.set("Computer selected " + computer)
        var2.set("Win!")

    elif computer == "scissors":
        var.set("Computer selected " + computer)
        var2.set("Lose!")

def Siccors():
    randompick = ['rock', 'paper', 'scissors']
    computer = (random.choice(randompick))
    if computer == "scissors":
        var.set("Computer selected " + computer)
        var2.set("Draw!")

    elif computer == "paper":
        var.set("Computer selected " + computer)
        var2.set("Win!")

    elif computer == "rock":
        var.set("Computer selected " + computer)
        var2.set("Lose!")

root = Tk()
var = StringVar()
var2 = StringVar()
label = Label(root, textvariable=var, relief=FLAT)
label2 = Label(root, textvariable=var2, relief=FLAT)

root.title("rock, paper scissors")
root.geometry("150x125")

app = Frame(root)
app.grid()
button1 = Button(app, text = "Rock", command = Rock)
button2 = Button(app, text = "Paper", command = Paper)
button3 = Button(app, text = "Siccors", command = Siccors)



button1.grid()
button2.grid()
button3.grid()
label.grid()
label2.grid()


root.mainloop()
