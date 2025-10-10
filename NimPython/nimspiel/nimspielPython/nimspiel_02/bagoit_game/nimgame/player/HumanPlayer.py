from bagoit_game.nimgame.player.INimgamePlayer import INimgamePlayer

class HumanPlayer (INimgamePlayer):
    def __init__(self, name="Human"):
        super().__init__(name)

    def do_turn(self, stones):
        print(f"Es sind noch {stones} Steine übrig. Bitte nimm Einen!")
        return int(input("Wieviele Steine nimmst du (1-3)? "))

    def get_name(self):
        return self.name