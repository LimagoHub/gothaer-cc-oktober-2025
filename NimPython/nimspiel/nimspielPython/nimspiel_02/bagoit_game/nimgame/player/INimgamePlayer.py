from abc import ABC, abstractmethod

from bagoit_game.player.IPlayer import IPlayer

class INimgamePlayer(IPlayer, ABC):
    
    def __init__(self, name="__class__.__name__"):
        self.name = name

    @abstractmethod
    def do_turn(self, stones):
        pass

    @abstractmethod
    def get_name(self):
        pass