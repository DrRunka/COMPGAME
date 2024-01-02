import pygame
import os
import importlib
import sys
import debug

# Dynamic Loader Function
import os
import importlib.util
import sys
from Level import Level


def dynamic_loader(directory, base_class):
    """
    Load all subclasses of a specified type from Python files in a given directory.

    Args:
    directory (str): The directory containing Python files to be scanned.
    base_class (type): The base class type to look for subclasses of.

    Returns:
    list: A list of classes which are subclasses of the specified base class.

    Side effects:
    - Loads modules found in the specified directory into sys.modules.
    - Dynamically imports Python files found in the directory.

    Expected runtime: Varies depending on the number of files and classes. Each file is imported and each class is inspected.
    """
    loaded_classes = []

    # Add the directory to sys.path for module resolution
    if directory not in sys.path:
        sys.path.insert(0, directory)

    for filename in os.listdir(directory):
        debug.out(filename)
        if filename.endswith('.py') and not filename.startswith('_'):
            file_path = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location("Level", file_path)
            mod = importlib.util.module_from_spec(spec)
            debug.out(dir(mod))
            spec.loader.exec_module(mod)


            # Check each class defined in the module
            for attribute_name in dir(mod):
                
                attribute = getattr(mod, attribute_name)
                if isinstance(attribute, type):
                    debug.out(f"Attribute: {attribute}")
                    debug.out(f"Base class: {base_class}")
                    debug.out(issubclass(attribute, base_class))
                if isinstance(attribute, type) and issubclass(attribute, base_class) and attribute is not base_class:
                    debug.out("Found class: " + attribute_name)
                    loaded_classes.append(attribute)

    return loaded_classes



# Main Game Class
class Game:
    def __init__(self, level_directory):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.levels = dynamic_loader(level_directory,Level)
        self.current_level_index = 0
        self.current_level = None
        self.running = True

    def run(self):
        """
        Start the game loop.
        """
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.WINDOWCLOSE:
                # if event.type == pygame.QUIT:
                    #intercept quit event and make it print help...
                    print("Printing Current Level's Help Dialog...")
                    self.current_level.help()
                    # self.running = False

            if self.current_level is None:
                if self.current_level_index < len(self.levels):
                    # Load the next level
                    self.current_level = self.levels[self.current_level_index](self)
                    
                    
                    title = f"Level {self.current_level_index + 1}: {self.current_level.__class__.__name__}"
                    #set window title
                    pygame.display.set_caption(title)
                    self.current_level.start()
                else:
                    print("All levels completed!")
                    break

            # Assuming self.current_level can be None if all levels are completed
            if self.current_level:
                result = self.current_level.update()
                if result == 'win':
                    self.current_level_index += 1
                    if self.current_level_index >= len(self.levels):
                        print("Game completed!")
                        break
                    self.current_level = None
                elif result == 'lose':
                    print("Level failed, retrying...")
                    self.current_level = None

            pygame.display.flip()

        pygame.quit()
# Example usage
if __name__ == "__main__":
    #load levels directory from command line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <levels_directory>")
        sys.exit(1)
    levels_directory = sys.argv[1]
    game = Game(levels_directory)
    game.run()
