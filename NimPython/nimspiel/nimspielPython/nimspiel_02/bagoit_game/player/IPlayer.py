from abc import ABC, abstractmethod

class IPlayer(ABC):
    

    def __init__(self, name="__class__.__name__"):
        self.name = name

    @abstractmethod
    def do_turn(self, board):
        pass

    @abstractmethod
    def get_name(self):
        pass