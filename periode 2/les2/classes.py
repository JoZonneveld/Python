class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player():
    def __init__(self, naam, x, y):
        self.naam = naam
        self.Position = Position(x, y)

    def printPlayer(self):
        print(self.naam, self.Position.x, self.Position.y)
