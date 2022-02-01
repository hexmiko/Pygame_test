import os
import pygame


class BackgroundPalarax:

    velocity = 0.5
    image = pygame.transform.scale(pygame.image.load(os.path.join('Sprites', 'space_bg.png')), (1000,480))
    largula = image.get_width()

    def __init__(self, y) -> None:
        self.y = y
        self.x1 = 0
        self.x2 = self.largula


    def mover(self):
        self.x1 -= self.velocity
        self.x2 -= self.velocity

        if self.x1 + self.largula < 0:
            self.x1 = self.x2 + self.largula
        if self.x2 + self.largula < 0:
            self.x2 = self.x1 + self.largula


    def desenhar(self, tela):
        self.mover()
        tela.blit(self.image, (self.x1, self.y))
        tela.blit(self.image, (self.x2, self.y))