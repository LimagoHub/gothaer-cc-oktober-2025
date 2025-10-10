
from bagoit_game.IGame import IGame

class Client:
    def __init__(self, game: IGame):
        self.game = game

    def go(self):
        self.game.play()