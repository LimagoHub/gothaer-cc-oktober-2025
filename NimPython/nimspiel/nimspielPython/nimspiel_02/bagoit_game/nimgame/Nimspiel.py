from bagoit_game.Game import Game

class Nimspiel(Game):

    def __init__(self, board=23):
        super().__init__(board)
        self.turn = -1

    def _update_board(self):
        self.board -= self.turn

    def _is_game_over(self) -> bool:
        return self.board < 1
    
    def _is_valid(self) -> bool:
        return self.turn >= 1 and self.turn <= 3
    

