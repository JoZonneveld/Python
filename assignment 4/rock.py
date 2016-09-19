import random
from tkinter import *

playerwins = 0
computerwins = 0

def Rock():
    randompick = ['rock', 'paper', 'scissors']
    computer = (random.choice(randompick))

    global computerwins
    global playerwins

    if computer == "rock":
        var.set("Computer selected " + computer)
        var2.set("You draw!")

    elif computer == "scissors":
        var.set("Computer selected " + computer)
        var2.set("You win!")
        playerwins += 1

    elif computer == "paper":
        var.set("Computer selected " + computer)
        var2.set("You lose!")
        computerwins += 1

def Paper():
    randompick = ['rock', 'paper', 'scissors']
    computer = (random.choice(randompick))

    global computerwins
    global playerwins

    if computer == "paper":
        var.set("Computer selected " + computer)
        var2.set("You draw!")

    elif computer == "rock":
        var.set("Computer selected " + computer)
        var2.set("You win!")
        playerwins += 1

    elif computer == "scissors":
        var.set("Computer selected " + computer)
        var2.set("You lose!")
        computerwins += 1

def scissors():
    randompick = ['rock', 'paper', 'scissors']
    computer = (random.choice(randompick))

    global computerwins
    global playerwins

    if computer == "scissors":
        var.set("Computer selected " + computer)
        var2.set("You draw!")

    elif computer == "paper":
        var.set("Computer selected " + computer)
        var2.set("You win!")
        playerwins += 1

    elif computer == "rock":
        var.set("Computer selected " + computer)
        var2.set("You lose!")
        computerwins += 1

root = Tk()
var = StringVar()
var2 = StringVar()
label = Label(root, textvariable=var, relief=FLAT)
label2 = Label(root, textvariable=var2, relief=FLAT)

<<<<<<< HEAD
var.set("Welcome to rock, paper scissors")

root.title("rock, paper sissors")
root.geometry("175x125")
=======
root.title("rock, paper scissors")
root.geometry("150x125")
>>>>>>> origin/master

app = Frame(root)
app.grid()
button1 = Button(app, text = "Rock", command = Rock)
button2 = Button(app, text = "Paper", command = Paper)
button3 = Button(app, text = "scissors", command = scissors)

button1.grid()
button2.grid()
button3.grid()
label.grid()
label2.grid()


root.mainloop()