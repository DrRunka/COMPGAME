import pygame
import random
from Level import Level  # Adjust the import path based on your project structure


class AnotherLevel(Level):  #deliberate name conflict
    def __init__(self, game):
        # print(f"Initializing Sample Level with args: {args} and kwargs: {kwargs}")
        super().__init__(game)
        self.font = pygame.font.Font(None, 36)
        self.win_button = pygame.Rect(100, 100, 200, 50)
        self.lose_button = pygame.Rect(100, 200, 200, 50)

    def start(self):
        print("Moving Sample Level")

    def draw_button(self, button_rect, text,color):
        pygame.draw.rect(self.game.screen, color, button_rect)  # Green button
        text_surface = self.font.render(text, True,color)  # White text
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.game.screen.blit(text_surface, text_rect)

    def update(self):
        self.game.screen.fill((0, 0, 0))  # Fill screen with black

        #move the win button a small amount in a random direction, but stay on screen
        self.win_button.move_ip(random.randint(-1,1),random.randint(-1,1))
        self.win_button.clamp_ip(self.game.screen.get_rect())

        
        #move the lose button a small amount in a random direction that is roughly towards the win button
        #get the win button location
        # win_button_center = self.win_button.center
        # #move the lose button towards the win button
        # if win_button_center[0] < self.lose_button.center[0]:
        #     self.lose_button.move_ip(-1,random.randint(-1,1))
        # else:
        #     self.lose_button.move_ip(1,random.randint(-1,1))
        self.lose_button.move_ip(random.randint(-1,1),random.randint(-1,1))
        


        # Draw buttons
        self.draw_button(self.win_button, "Win", (0,128, 0))
        self.draw_button(self.lose_button, "Lose", (128,0,0))

        # Event handling for buttons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.win_button.collidepoint(event.pos):
                    return 'win'
                elif self.lose_button.collidepoint(event.pos):
                    return 'lose'

        return None  # Continue the level if no button is clicked
