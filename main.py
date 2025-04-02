import pygame #lo instalamos en la terminal haciendo pip install pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
