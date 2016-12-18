class rekenen():

    def __init__(self, getal1, getal2):
        self.getal1 = getal1
        self.getal2 = getal2

    def plus(self):
        print(self.getal1+ self.getal2)
    
    def min(self):
        print(self.getal1 - self.getal2)

getal = rekenen(
                    int(input("Voer iets in: ")),
                    int(input("Voer iets in: "))
                )

getal.plus()
getal.min()
