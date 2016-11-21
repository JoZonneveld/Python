class Game():
    def __init__(self, title, player1, player2):
        self.title = title
        self.player1 = player1
        self.player2 = player2

    def printGame(self):
        print(self.title, self.player1, self.player2)

title = input("Voer een titel in: ")
player1 = input("Voer een player1 naam in: ")
player2 = input("Voer een player2 naam in: ")

game1 = Game(title, player1, player2)

game1.printGame()
