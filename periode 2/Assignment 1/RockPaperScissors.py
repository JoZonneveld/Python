import random

class Player:
    def __init__(self, naam, score):
        self.naam = naam
        self.score = score

    def increaseScore(self, amount):
        self.score = self.score + amount

class RockPaperScissors:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def pick(self):
        play1 = Player(self.player1, 0)
        play2 = Player(self.player2, 0)

        while play2.score !=2 and play1.score !=2:

            randompick = [0, 1, 2]
            #0 = rock
            #1 = paper
            #2 = scissors
            player1pick = (random.choice(randompick))
            player2pick = (random.choice(randompick))

            if player1pick == player2pick:
                print("draw")
            elif player1pick == 0 and player2pick == 1:
                print("Player 1 pakt rock, Player 2 pakt paper. P2 wint")
                play2.increaseScore(1)
            elif player1pick == 0 and player2pick == 2:
                print("Player 1 pakt rock, Player 2 pakt scissors. P1 wint")
                play1.increaseScore(1)
            elif player1pick == 1 and player2pick == 0:
                print("Player 1 pakt paper, Player 2 pakt rock. P1 wint")
                play1.increaseScore(1)
            elif player1pick == 1 and player2pick == 2:
                print("Player 1 pakt paper, Player 2 pakt scissors. P2 wint")
                play2.increaseScore(1)
            elif player1pick == 2 and player2pick == 0:
                print("Player 1 pakt scissors, Player 2 pakt rock. P2 wint")
                play2.increaseScore(1)
            elif player1pick == 2 and player2pick == 1:
                print("Player 1 pakt scissors, Player 2 pakt paper. P1 wint")
                play1.increaseScore(1)

            scorep1 = play1.score
            scorep2 = play2.score
            if scorep2 !=2 and scorep1 !=2:
                print("Stand P1:", scorep1, " - P2:", scorep2)
        print("Eindstand P1:", scorep1, " - P2:", scorep2)
        if scorep1 > scorep2:

            if play1.score != 2 and play2.score != 2:
                print("Stand P1:", play1.score, " - P2:", play2.score)


        print("Eindstand P1:", play1.score, " - P2:", play2.score)
        if play1.score > play2.score:

            print("P1 Wint!!!")
        else:
            print("P2 Wint!!!")

game = RockPaperScissors("test", "test1")

game.pick()
