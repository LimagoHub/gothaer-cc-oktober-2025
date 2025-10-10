from abc import ABC, abstractmethod

class IGame(ABC):
    
    @abstractmethod
    def play(self):
        """
        Abstract method that must be implemented by subclasses.
        This method should contain the main game logic.
        """
        pass