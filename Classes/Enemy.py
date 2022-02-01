import os
import pygame
from interfaces import GameObject, Enemy as EnemyInterface


class Enemy(GameObject):

    velocity = 7
    
    
    def __init__(self, x: int, y: int) -> None:
        
        super().__init__(x, y)
        self.image = pygame.image.load(os.path.join('Sprites', 'Square_Enemy.png'))
    

    def mover(self):
        self.x -= self.velocity


    def draw(self, tela):
        tela.blit(self.image, (self.x, self.y))
        #self.image = pygame.transform.rotate(self.image, -0.01)


    def get_mask(self):
        return pygame.mask.from_surface(self.image)


    def check_collision(self, object: GameObject):
        mascara_da_object = object.get_mask()
        mascara_do_enemy = self.get_mask()

        distancia_dos_dois = (self.x - object.x, self.y - object.y)

        ponto_da_colicao_eu_acho = mascara_da_object.overlap(mascara_do_enemy, distancia_dos_dois)

        if ponto_da_colicao_eu_acho:
            return True
        else:
            return False
