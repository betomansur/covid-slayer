import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 550
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')


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
#####PONTOS######
#assets gemas
#gemab_img = pygame.image.load('img/gemas/hab b.png').convert_alpha()
#gemay_img = pygame.image.load('img/gemas/hab y.png').convert_alpha()
#gemag_img = pygame.image.load('img/gemas/hab g.png').convert_alpha()
#t_gemas = [gemab_img, gemay_img, gemag_img]
#################
#assets chão
chao_img = pygame.image.load("Sprites/plataforma.png").convert_alpha()
chao_img = pygame.transform.scale(chao_img, (710, 200))
#assets background
bg = pygame.image.load("Sprites/hospital2.png.jpg").convert()
background = pygame.transform.scale(bg, (700, 620))
background_rect = background.get_rect()
#assets do tiro
bullet_img = pygame.image.load('Sprites/laserRed16.png').convert_alpha()
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
        self.rect.centerx = 400
        self.rect.bottom = HEIGHT-20
        self.speedx = 0
        self.speedy = 0
        self.lifes = VIDAS
        self.sprites = all_sprites
        self.bullets = all_bullets
        self.tiro  = bullet_img
    
    def update(self):

        #Movimentação em y
        self.speedy += GRAVITY
        #Atualiza a posição y
        self.rect.y += self.speedy
        #Atualiza a posição x
        self.rect.x += self.speedx
        
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

    #Função do tiro
    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bullet = Bullet(self.tiro, self.rect.bottom, self.rect.centerx)
        self.bullets.add(new_bullet)
        self.sprites.add(new_bullet)

#Classe do inimigo
class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        pygame.sprite.Sprite.__init__(self)
        
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 20
        self.rect.centery = HEIGHT - 20
        self.speedx = 0
        self.speedy = 0
    
    #inimigo se move
    def update(self):
        self.rect.x += 4
        if self.rect.left > WIDTH:
            self.rect.right = -100   

#Classe do tiro
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = bullet_img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = 20 #Velocidade fixa pro lado

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left > WIDTH:
            self.kill()

game = True
#Cria um relógio que conta o tempo em jogo
tempo = pygame.time.Clock()
FPS = 20

#############COLISõES#############
#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
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
                    player.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    player.speedx += 8
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.shoot()
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speedx = 0

        hits = pygame.sprite.spritecollide(player, collide_enemy, True, pygame.sprite.collide_mask)
        hit2 = pygame.sprite.groupcollide(all_bullets, collide_enemy, True, True)

        if len(hits) > 0:
            VIDAS -= 1
            enemy.rect.x = -200
            all_sprites.add(enemy)
            collide_enemy.add(enemy)
        if len(hit2) > 0:
            enemy.rect.x = -200
            all_sprites.add(enemy)
            collide_enemy.add(enemy)

        all_sprites.update()
        collide_enemy.update()
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background, (0, 0))
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

    if VIDAS<1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = False
            

    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados