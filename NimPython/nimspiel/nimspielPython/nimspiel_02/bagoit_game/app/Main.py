from bagoit_game.nimgame.Nimspiel import Nimspiel
from bagoit_game.client.Client import Client
from bagoit_game.nimgame.player.HumanPlayer import HumanPlayer
from bagoit_game.nimgame.player.ComputerPlayer import ComputerPlayer

def main():
    game = Nimspiel()
    game.add_player(HumanPlayer("Human"))
    game.add_player(ComputerPlayer("Computer"))
    client = Client(game)
    client.go()

if __name__ == "__main__":
    main()