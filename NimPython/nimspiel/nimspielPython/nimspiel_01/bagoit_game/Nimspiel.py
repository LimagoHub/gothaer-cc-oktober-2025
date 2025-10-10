from bagoit_game.IGame import IGame

class Nimspiel(IGame):

    def __init__(self, steine=23):
        self.steine = steine


    def play(self):
        while not self._isGameOver():
            self._playRound()
            print()


    def _playRound(self):
        self._spielerzug()
        print()
        self._computerzug()
        print()


    def _spielerzug(self):
        zug = 0
        while True:
            print(f"Es sind noch {self.steine} Steine übrig. Bitte nimm Einen!")
            zug = int(input("Wieviele Steine nimmst du (1-3)? "))
            if zug < 1 or zug > 3:
                print("Ungültiger Zug. Bitte 1, 2 oder 3 Steine nehmen.")
            else:
                break
        self.steine -= zug


    def _computerzug(self):
        zuege = [3, 1, 1, 2]
        if(self._isGameOver()):
            print("Human hat verloren")
            return
        if (self.steine == 1):
            print("Computer hat verloren")
            self.steine = 0
            return
        zug = zuege[self.steine % 4]
        print(f"Computer nimmt {zug} Steine.")
        self.steine -= zug



    def _isGameOver(self):
        return self.steine <= 0