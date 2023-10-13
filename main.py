import pygame
import game



if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1200,700))
    pygame.display.set_caption("Dastan")
    
    dastan = game.Game()

    clock = pygame.time.Clock()

    play = True

    while play:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        screen.blit(dastan.draw(), (0, 0)) 
        pygame.display.update()


    pygame.quit()


