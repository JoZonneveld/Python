import random

stop = 0
name = (input("whats your name? \n"))
playerwins = 0
computerwins = 0
print("Welcome ", name)
while stop == 0:
    pick = (input("whats your pick? \n"))

    randompick = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    computer = (random.choice(randompick))

    if pick == computer:
        print("Draw!")
    else:
        if pick == "rock":
            if computer == "lizard":
                print(pick, " crushes ", computer)
                playerwins = playerwins + 1
            elif computer == "scissors":
                print(pick, " crushes ", computer)
                playerwins = playerwins + 1
            elif computer == "spock":
                print(computer, " vaporizes ", pick)
                computerwins = computerwins + 1
            elif computer == "paper":
                print(computer, " covers ", pick)
                computerwins = computerwins + 1

        if pick == "paper":
            if computer == "rock":
                print(pick, " covers ", computer)
                playerwins = playerwins + 1
            elif computer == "spock":
                print(pick, " disaproves ", computer)
                playerwins = playerwins + 1
            elif computer == "scissors":
                print(computer, " cuts ", pick)
                computerwins = computerwins + 1
            elif computer == "lizard":
                print(computer, " eats ", pick)
                computerwins = computerwins + 1

        if pick == "scissors":
            if computer == "paper":
                print(pick, " cuts ", computer)
                playerwins = playerwins + 1
            elif computer == "lizard":
                print(pick, " decapitates ", computer)
                playerwins = playerwins + 1
            elif computer == "spock":
                print(computer, " smashes ", pick)
                computerwins = computerwins + 1
            elif computer == "rock":
                print(computer, " crushes ", pick)
                computerwins = computerwins + 1

        if pick == "lizard":
            if computer == "paper":
                print(pick, " eats ", computer)
                playerwins = playerwins + 1
            elif computer == "spock":
                print(pick, " poisens ", computer)
                playerwins = playerwins + 1
            elif computer == "rock":
                print(computer, " crushes ", pick)
                computerwins = computerwins + 1
            elif computer == "scissors":
                print(computer, " decapitates ", pick)
                computerwins = computerwins + 1

        if pick == "spock":
            if computer == "scissors":
                print(pick, " smashes ", computer)
                playerwins = playerwins + 1
            elif computer == "rock":
                print(pick, " vaporizes ", computer)
                playerwins = playerwins + 1
            elif computer == "lizard":
                print(computer, " poisens ", pick)
                computerwins = computerwins + 1
            elif computer == "paper":
                print(computer, " disaproves ", pick)
                computerwins = computerwins + 1

    print("Standings ", playerwins, " - ", computerwins)

    END = (input("Do you want to stop? N=No, Y=Yes \n"))
#
    if END == "y":
        stop = 1