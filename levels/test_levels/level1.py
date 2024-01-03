import pygame
from Level import Level  # Adjust the import path based on your project structure


class SampleLevel(Level):
    def __init__(self, game):
        # print(f"Initializing Sample Level with args: {args} and kwargs: {kwargs}")
        super().__init__(game)
        self.font = pygame.font.Font(None, 36)
        self.win_button = pygame.Rect(100, 100, 200, 50)
        self.lose_button = pygame.Rect(100, 200, 200, 50)

    def start(self):
        print("Starting Sample Level")

    def draw_button(self, button_rect, text):
        pygame.draw.rect(self.game.screen, (0, 128, 0), button_rect)  # Green button
        text_surface = self.font.render(text, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.game.screen.blit(text_surface, text_rect)

    def update(self):
        self.game.screen.fill((0, 0, 0))  # Fill screen with black

        # Draw buttons
        self.draw_button(self.win_button, "Win")
        self.draw_button(self.lose_button, "Lose")

        # Event handling for buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.win_button.collidepoint(event.pos):
                    return 'win'
                elif self.lose_button.collidepoint(event.pos):
                    return 'lose'

        return None  # Continue the level if no button is clicked
