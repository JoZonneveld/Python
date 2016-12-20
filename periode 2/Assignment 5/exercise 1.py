class Player:
    def __init__(self, name):
        self.Name = name
        self.LP = 10

    def Heal(self):
        self.LP += 1
        return self.LP

    def Damage(self):
        self.LP -= 1
        return self.LP

class Game:
    def __init__(self, player1, player2):
        self.Player1 = player1
        self.Player2 = player2

    def Cheat(self):
        player1 = Player(self.Player1)
        player2 = Player(self.Player2)

        print(player1.Heal())
        print(player2.Damage())

game = Game("Joost", "Roos")

game.Cheat()
