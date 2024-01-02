from abc import abstractmethod

# Base Level Class
class Level():
    """
    Abstract base class for game levels.
    Each level should subclass this and implement the abstract methods.
    """
    def __init__(self, game, *args, **kwargs):
        self.game = game

    @abstractmethod
    def start(self):
        """
        Start the level. Initialize level-specific elements here.
        """
        pass

    @abstractmethod
    def update(self):
        """
        Update the level. This method is called once per frame.
        It should return 'win' or 'lose' based on the game state.
        """
        pass

    def help(self):
        """
        Print a help dialog for the level.
        """
        print(f"Help for {self.__class__.__name__}")
        print("This level has no help dialog. :(")
        
        