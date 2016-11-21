import random
class Player:
    def __init__(self, naam, score):
        self.naam = naam
        self.score = score

class RockPaperScissors:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def pick(self, player1pick, player2pick):
        #0 = rock
        #1 = paper
        #2 = scissors
        if player1pick == player2pick:
            print("draw")
        elif player1pick == 0 and player2pick == 1:
            print("Player2 wins")
        elif player1pick == 0 and player2pick == 2:
            print("Player1 wins")
        elif player1pick == 1 and player2pick == 0:
            print("Player1 wins")
        elif player1pick == 1 and player2pick == 2:
            print("Player2 wins")
        elif player1pick == 2 and player2pick == 0:
            print("Player2 wins")
        elif player1pick == 2 and player2pick == 1:
            print("Player1 wins")

game = RockPaperScissors("player1", "player2")

randompick = [0, 1, 2]
player1pick = (random.choice(randompick))
player2pick = (random.choice(randompick))

game.pick(player1pick, player2pick)
