import pygame

pygame.font.init()
tamanho_fonte = 15
FONTE_PONTOS = pygame.font.SysFont('arial', tamanho_fonte)

def desenharTexto(tela, informacao, xyTuple: tuple):
    texto = FONTE_PONTOS.render(informacao, 1, (255, 255, 255))
    tela.blit(texto, xyTuple)
