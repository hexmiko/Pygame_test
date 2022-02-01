import os
import pygame
from interfaces import GameObject


class Player(GameObject):
    """ Objeto que o usuário controla para jogar o Game """

    IMAGEM = pygame.transform.rotate(
        pygame.image.load(
            os.path.join(
                'Sprites', 'Triangule_Player.png'
                )
            ), -90
        )


    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y
        self.velocity = 9
    

    def moveDown(self):
        self.y += self.velocity
        if self.y >= 480 - self.IMAGEM.get_height(): # talvez seja bom pegar a tela logo quando instancia o Player
            self.y = 480 - self.IMAGEM.get_height()
    
    def moveUp(self):
        self.y -= self.velocity
        if self.y <= 0:
            self.y = 0
    

    def draw(self, tela):
        tela.blit(self.IMAGEM, (self.x, self.y))


    def get_mask(self):
        return pygame.mask.from_surface(self.image)


    def check_collision(self, objeto):
        mascara_do_objeto = objeto.get_mask()
        mascara_do_player = pygame.mask.from_surface(self.IMAGEM)

        distancia_dos_dois = (self.x - objeto.x, self.y - objeto.y)

        ponto_da_colicao_eu_acho = mascara_do_objeto.overlap(mascara_do_player, distancia_dos_dois)

        if ponto_da_colicao_eu_acho:
            return True
        else:
            return False

