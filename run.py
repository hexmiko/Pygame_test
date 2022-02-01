from time import sleep
import pygame
from Classes import Player, Bala, Enemy, Spawner, Label, BackgroundPalarax, Hunter




def gameoverScene():
    screen.fill((0, 0, 0))
    Label.desenharTexto(screen, "GAMA OVER DA!!", (size[0]/2 - 60, size[1]/2))
    pygame.display.update()

def fechar_game():
    global running
    running = False
    gameoverScene()
    sleep(2)
    pygame.quit()
    quit()


# Variaveis para nao ter tantos numeros soltos
limite_balas = 5
time_per_level = 30 # Segundos
cooldown_enemy = 0.75


# Preparando o jogo
pygame.init()
pygame.display.set_caption('Asteroid Test')

running = True
size = width, height = 1000, 480
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
relogio = pygame.time.Clock()

listadebalas = []
listadeenemys = []

jogador = Player(15, 10)
pontos = 0
spawn_enemy = Spawner(1000, 460, Enemy, listadeenemys)
spawn_hunter = Spawner(1000, 460, Hunter, listadeenemys)
bg = BackgroundPalarax(0)


while True:
    relogio.tick(30)
    time_now_seconds = pygame.time.get_ticks() // 1000


    # Checando Inputs
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        jogador.moveDown()

    elif keys[pygame.K_w]:
        jogador.moveUp()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fechar_game()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                fechar_game()

            elif event.key == pygame.K_SPACE:

                if not len(listadebalas) >= limite_balas:
                    bala = Bala(jogador.x, jogador.y + 8)
                    listadebalas.append(bala)



    #Spawnae enemy
    spawn_enemy.random_spawn_y(cooldown_enemy)
    spawn_hunter.spawnar_hunter(jogador, cooldown_enemy * 2)
    



    # Draw
    
    if running:
        bg.desenhar(screen)
        jogador.draw(screen)
        Label.desenharTexto(screen, f'Pontos: {pontos}', (12, 10))
        Label.desenharTexto(screen, f'Enemys: {len(listadeenemys)}', (150, 10))
        Label.desenharTexto(screen, f'Balas: {len(listadebalas)}', (150*2, 10))
        Label.desenharTexto(screen, f'Tempo: {time_per_level - time_now_seconds - 1}s', (150*3, 10))

        if listadebalas:
            for bala in listadebalas:

                bala.mover()
                bala.draw(screen)

                if bala.x >= size[0]: # Depois fazer essa verificação na propria classe
                    listadebalas.remove(bala)
        
        if listadeenemys:
            for enemy in listadeenemys:

                enemy.mover()
                enemy.draw(screen)

                if enemy.x <= 0:
                    listadeenemys.remove(enemy)

        # Checar colisão
        for enemy in listadeenemys:

            if jogador.check_collision(enemy):
                print('Colidiu com um Inimigo')
                fechar_game()


            for bala in listadebalas:
                if enemy.check_collision(bala):
                    listadebalas.remove(bala)
                    listadeenemys.remove(enemy)
                    pontos += 1
        

        if time_now_seconds >= time_per_level:
            fechar_game()
    else:
        ### Em teoria aqui devia ficar a tela de inicio de jogo
        pass

    pygame.display.update()
