import os
import pygame
from interfaces import GameObject


class Bala(GameObject):
    """ Depois de criada so tem que ir reto e verificar se tococou em algo ou saiu da tela """

    velocity = 13
    limite_tela_x = 1000

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join('Sprites', 'pixilart-drawing.png'))
    

    def mover(self):
        self.x += self.velocity

    
    def draw(self, tela):
        tela.blit(self.image, (self.x, self.y))
        # Girar bala -> self.image = pygame.transform.rotate(self.image, -1)


    def get_mask(self):
        return pygame.mask.from_surface(self.image)
