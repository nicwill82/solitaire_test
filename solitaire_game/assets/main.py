import pygame
from src.game import Solitaire_Game
#from assets.src.game import Solitaire_Game


def run_game():
    # Initialize Pygame
    pygame.init()

    # Set up the window dimensions
    width, height = 800, 600

    # Create the game window
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Solitaire")

    # Create an instance of the Solitaire game
    game = SolitaireGame(window)

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the game state
        game.update()

        # Render the game
        game.render()

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

# Run the game
if __name__ == '__main__':
    run_game()
