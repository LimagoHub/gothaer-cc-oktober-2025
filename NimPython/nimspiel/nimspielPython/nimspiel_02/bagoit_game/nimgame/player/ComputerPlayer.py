from bagoit_game.nimgame.player.INimgamePlayer import INimgamePlayer

class ComputerPlayer (INimgamePlayer):
    def __init__(self, name="Computer"):
        super().__init__(name)

    def do_turn(self, stones):
        zuege = [3, 1, 1, 2]
        zug = zuege[stones % 4]
        print(f"Computer nimmt {zug} Steine.")
        return zug

    def get_name(self):
        return self.name