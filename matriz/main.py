import pygame
import sys
from brick import Brick
import random 
from quebravel import Bloco_q

pygame.init()

#FPS DO JOGO
clock = pygame.time.Clock()
FPS = 30

#MEDIDAS DO JOGO
WIDTH = 750
HEIGHT = 650
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AtomicKingdom')

#CONSTANTES DE ALTURA E LARGURA
PLAYER_WIDTH = 45
PLAYER_HEIGHT = 40
BRICK_WIDTH=50
BRICK_HEIGHT=50
QUEBRAVEL_WIDTH=50
QUEBRAVEL_HEIGHT=50
BOMB_WIDTH=90
BOMB_HEIGHT=90
EXP_WIDTH=100
EXP_HEIGHT=100

#IMAGENS DOS BLOCOS E PERSONAGENS
brick_img = pygame.image.load('assets/Bloco_Fixo.jpg')
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT))
quebravel_img = pygame.image.load('assets/quebravel.png')
quebravel_img =  pygame.transform.scale(quebravel_img, (QUEBRAVEL_WIDTH, QUEBRAVEL_HEIGHT))
conjunto_bomba = []


"""LÓGICA DO JOGO EM FORMA DE MATRIZ"""
LAYOUT = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1],
    [1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,6,1,],
    [1, -1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,-1,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, -1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,-1,1],
    [1, 5, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,-1,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1],
        ]



# Criando um grupo de blocos 
todos_quebraveis = pygame.sprite.Group()
todos_fixos = pygame.sprite.Group()
todos_blocos = pygame.sprite.Group()

# Criando um grupo de sprites
todos_sprites = pygame.sprite.Group()
todas_bombas = pygame.sprite.Group()
todos_players = pygame.sprite.Group()



def desenhar_mapa():
    for l in range (len(LAYOUT)):
            for c in range (len(LAYOUT[l])):
                item = LAYOUT[l][c]
                
                if item == 1:
                    pedra = Brick(brick_img,c,l,BRICK_WIDTH,BRICK_HEIGHT)
                    todos_fixos.add(pedra)
                
                if item == 0:
                    r= random.randint(2,4)
                    if r ==3 or r==4:
                        madeira = Bloco_q(quebravel_img,c,l,QUEBRAVEL_WIDTH,QUEBRAVEL_HEIGHT)
                        todos_quebraveis.add(madeira)
                        LAYOUT[l][c] = 1
                    else:
                        LAYOUT[l][c] = 0

                if item == 5 :

                    LAYOUT[l][c] = 0
                    # player1 = Player1(boneco_img, all_sprites, all_bombs,c,l,imagem)
                    
                
                if item == 6:
                    LAYOUT[l][c] = 0
                    # player2 = Player2(boneco1_img,all_sprites, all_bombs,c,l,imagem)

# adicionando aos grupos de sprites
# todos_sprites.add(player1)
# todos_sprites.add(player2)
todos_sprites.add(todos_fixos)
todos_sprites.add(todos_quebraveis)
todos_blocos.add(todos_fixos)
todos_blocos.add(todos_quebraveis)
# todos_players.add(player1)
# todos_players.add(player2)
def jogo():
    #DESENHA TODO O MAPA 
    desenhar_mapa()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        tela.fill((101, 214, 102))  # PREENCHER A TELA DE VERDE

        # Desenha os blocos
        todos_fixos.draw(tela)
        todos_quebraveis.draw(tela)

        pygame.display.update()  # Atualiza a tela

jogo()  # Chama a função para iniciar o loop do jogo
