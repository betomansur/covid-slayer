import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nome não definido ainda')


# ----- Inicia assets
##Os nomes das variáveis está em uma mistura de português e inglês##
#assets jogador
JOG_WIDTH = 90
JOG_HEIGHT = 70
jog_img = pygame.image.load('Sprites/jogador1.png').convert_alpha()
jog_img = pygame.transform.scale(jog_img, (JOG_WIDTH, JOG_HEIGHT))
#assets inimigo
inim_img = pygame.image.load('Sprites/bacteria1.png').convert_alpha()
inim_img = pygame.transform.scale(inim_img, (70, 70))
#assets boss
boss_img = pygame.image.load('Sprites/bacteria1.png').convert_alpha()
boss_img = pygame.transform.scale(boss_img, (70, 70))
#####PONTOS######
#assets gemas
#gemab_img = pygame.image.load('img/gemas/hab b.png').convert_alpha()
#gemay_img = pygame.image.load('img/gemas/hab y.png').convert_alpha()
#gemag_img = pygame.image.load('img/gemas/hab g.png').convert_alpha()
#t_gemas = [gemab_img, gemay_img, gemag_img]
#################
#assets chão
#chao_img = pygame.image.load("sprite do chão").convert_alpha()
#chao_img = pygame.transform.scale(chao_img, (710, 200))
#assets background
#background = pygame.image.load('sprite do fundo').convert()
#background = pygame.transform.scale(background, (700, 620))
#background_rect = background.get_rect()
###FONTE DE TEXTO QUE O ANDREW TINHA DISPONIBILIZADO###
#assets fonte de texto
score_font = pygame.font.Font('font/PressStart2P.ttf', 28)


########EXTRAS#########
# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
# Define valores iniciais
GRAVITY = 6
PONTOS = 0
VIDAS = 3
#######################

#Classe do jogador
class jogador(pygame.sprite.Sprite):
    def __init__(self, jog_img, VIDAS):
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL
        self.image = jog_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = 580
        self.speedx = 0
        self.speedy = 0
        self.lifes = VIDAS
    
    def update(self):

        #Movimentação em y
        self.speedy += GRAVITY
        #Atualiza a posição y
        self.rect.y += self.speedy
        #Atualiza a posição x
        self.rect.x += self.speedx

        #Se jogador colidiu com algum inimigo
        collisions = pygame.sprite.spritecollide(self, inimigo, False)
        #Perde uma vida
        for collision in collisions:
            self.lifes -= 1
        
        #Corrige a posição para não sair da janela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 4
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.speedy = 0
            self.state = STILL

    #Método que faz o personagem pular
    def jump(self):
        #Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 50
            self.state = JUMPING    

#Classe do inimigo
class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        pygame.sprite.Sprite.__init__(self)
        
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 400
        self.speedx = 0
        self.speedy = 0
    
    #inimigo se move
    def update(self):
        self.rect.x += 4
        if self.rect.left > WIDTH:
            self.rect.right = -100   



game = True
#Cria um relógio que conta o tempo em jogo
tempo = pygame.time.Clock()
FPS = 20

#############COLISõES#############
#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
collide_enemy = pygame.sprite.Group()
# Criando o jogador, inimigo e gemas
player = jogador(jog_img, VIDAS)
enemy = inimigo(inim_img)
#Adicionando sprites em uma variável global
all_sprites.add(player)
all_sprites.add(enemy)
collide_enemy.add(enemy)
###################################

# ===== Loop principal =====
while game:
    if VIDAS > 0:
        tempo.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx -= 9
                if event.key == pygame.K_RIGHT:
                    player.speedx += 9
                elif event.key == pygame.K_UP:
                    player.jump()
            # Verifica se soltou alguma tecla.
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #        player.image = pygame.image.load('img/jogador1.png').convert_alpha()
            #        player.speedx = 0


        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        #window.blit(background, (0, 0))
        # Desenhando as sprites
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = score_font.render("{:06d}".format(PONTOS), True, (255, 0, 200))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (90,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = score_font.render(chr(9829) * VIDAS, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados