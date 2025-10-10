from bagoit_game.IGame import IGame
from bagoit_game.player.IPlayer import IPlayer


class Game(IGame):


    def __init__(self, board=None):
        self._curent_player = None
        self.players: list[IPlayer] = []
        self.board = board
        self.turn = None

    def get_board(self):
        return self.board
    
    def set_board(self, board):
        self.board = board

    def get_turn(self):
        return self.turn
    
    def set_turn(self, turn):
        self.turn = turn

    def add_player(self, player: IPlayer):
        self.players.append(player)


    def remove_player(self, player: IPlayer):
        self.players.remove(player)


    def play(self):
        while not self._is_game_over():
            self._playRound()
            print()


    # Integration Methode
    def _playRound(self):
        for i in range (0, len(self.players)):
            self._curent_player = self.players[i]
            self._play_single_turn()
            print()


    def _play_single_turn(self):
        if (self._is_game_over()):
            return
        self._execute_turn()
        self._terminate_turn()

    def _execute_turn(self):
        running = True
        while running:
            self.turn = self._curent_player.do_turn(self.board)
            running = self._turn_is_not_valid_turn()

    def _turn_is_not_valid_turn(self):
        if (self._is_valid()):
            return False
        print("Ungültiger Zug.")
        return True
    
    def _terminate_turn(self):
        self._update_board()
        self._print_game_over_message_if_game_is_over()


    def _print_game_over_message_if_game_is_over(self):
        if (self._is_game_over()):
            print(f"{self._curent_player.name} hat verloren")


    def _update_board(self):
        pass

    def _is_game_over(self) -> bool:
        pass
    
    def _is_valid(self) -> bool:
        pass
        