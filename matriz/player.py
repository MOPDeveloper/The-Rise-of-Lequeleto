import pygame

class Player:
    def __init__(self,img,todos_sprites,todas_bombas,x,y,largura,altura,conjunto_bomba):
        pygame.sprite.Sprite.__init__(self)

        #SPRITES E IMAGENS DO JOGADOR E DA BOMBA
        self.imagem = img
        self.todas_sprites = todos_sprites
        self.todas_bombas = todas_bombas
        self.rect = self.imagem.get_rect()
        
        #POSIÇÕES 
        self.x = x
        self.y = y
        self.rect.x = x*largura
        self.rect.y = y*altura

        #CONJUNTO ONDE FICA A IMAGEM DA ANIMAÇÃO DA BOMBA E DA EXPLOSAO
        self.conjunto_bomba = conjunto_bomba

        #SEGUNDOS PARA PODER SOLTAR OUTRA BOMBA
        self.ultima_bomba = pygame.time.get_ticks()
        self.tempo_limite = 3000 #3 SEGUNDOS PARA SOLTAR OUTRA BOMBA

    def update(self):
        # ATUALIZA POSIÇÃO
            self.rect.x = self.x*BRICK_WIDTH
            self.rect.y = self.y*BRICK_HEIGHT

    def soltar_bomba(self):
        tempo_atual = pygame.time.get_ticks()

        # SE O TEMPO ATUAL MENOS O TEMPO QUE FOI LANÇADO A ULTIMA BOMBA FOR MAIOR QUE O LIMITE ELE LANÇA OUTRA BOMBA
        if tempo_atual - self.ultima_bomba >= self.tempo_limite:

            #ULTIMA BOMBA VIRA O TEMPO ATUAL E CRIA UMA NOVA BOMVA
            self.ultima_bomba = tempo_atual
            nova_bomba = Bomba()

            self.todas_bombas.add(nova_bomba)
            self.todas_sprites.add(self.todas_bombas)

    def colidir_coletavel(self):
         '''FAZER AINDA COLETAVEL'''
         pass