from bagoit_game.Nimspiel import Nimspiel
from bagoit_game.Client import Client

def main():
    game = Nimspiel()
    client = Client(game)
    client.go()

if __name__ == "__main__":
    main()