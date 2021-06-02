import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 550
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame')


# ----- Inicia assets
##Os nomes das variáveis está em uma mistura de português e inglês##
#assets jogador
JOG_WIDTH = 90
JOG_HEIGHT = 70

jog_img = pygame.image.load('Sprites/gunman.png').convert_alpha()
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
go = pygame.image.load("Sprites/gameover.jpg").convert()
background = pygame.transform.scale(bg, (1000, 550))
background_rect = background.get_rect()

gameover = pygame.transform.scale(go, (1000, 550))
#assets do tiro

bullet_img = pygame.image.load('Sprites/vacina11111-removebg-preview.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (50, 20))

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
VIDAS2= 3
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
        new_bullet = Bullet(self.tiro, self.rect.centery, self.rect.centerx+40)
        self.bullets.add(new_bullet)
        self.sprites.add(new_bullet)

class jogador2(pygame.sprite.Sprite):
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
        new_bullet = Bullet(self.tiro, self.rect.centery, self.rect.centerx+40)
        self.bullets.add(new_bullet)
        self.sprites.add(new_bullet)


#Classe do inimigo
class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        pygame.sprite.Sprite.__init__(self)
        
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 70)
        self.rect.y = random.randint(-20, HEIGHT)
        self.speedx = random.randint(10, 12)
        self.speedy = random.randint(10, 11)

    
    #inimigo se move
    def update(self): 
        self.rect.x += 10
        if self.rect.top > HEIGHT or self.rect.right  < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, 70)  
            self.rect.y = random.randint(  20,550)  
             




          
          

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
        self.speedx = 100 #Velocidade fixa pro lado

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

#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
collide_enemy = pygame.sprite.Group()
# Criando o jogador, inimigo e gemas
player = jogador(jog_img, VIDAS)
player2 = jogador2(jog_img, VIDAS2)
all_sprites.add(player)

for i in range(0,8):
    enemy = inimigo(inim_img)
    all_sprites.add(enemy) 
    collide_enemy.add(enemy)   

#------ Tela de inicio
game=False
tela_inicial = True
while tela_inicial:
    # ----- Gera saídas
    window.blit(background, (0, 0))
    pygame.draw.rect(window, (0,0,0), [335, 250, 350, 60]) #[eixox, eixoy, raio, grossura]
    pygame.draw.rect(window, (0,0,0), [335, 320, 350, 60])
    pygame.draw.rect(window, (0,0,0), [335, 390, 350, 60])
    #Desenha nome do jogo
    text_inic = score_font.render("Covid Slay", True, (255, 0, 0))
    text_inic_rect = text_inic.get_rect()
    text_inic_rect.midtop = (500,  160)
    window.blit(text_inic, text_inic_rect)
    #Opção 1 jogador
    text_inic = score_font.render("1 Jogador", True, (255, 0, 0))
    text_inic_rect = text_inic.get_rect()
    text_inic_rect.midtop = (510,  270)
    window.blit(text_inic, text_inic_rect)
    #Opção 2 jogadores
    text_inic = score_font.render("2 Jogadores", True, (255, 0, 0))
    text_inic_rect = text_inic.get_rect()
    text_inic_rect.midtop = (510,  340)
    window.blit(text_inic, text_inic_rect)
    #Créditos 
    text_inic = score_font.render("Créditos", True, (255, 0, 0))
    text_inic_rect = text_inic.get_rect()
    text_inic_rect.midtop = (510,  410)
    window.blit(text_inic, text_inic_rect)
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                tela_inicial = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if pygame.mouse.get_pressed():
                print(pygame.mouse.get_pos())
                if pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=251 and pygame.mouse.get_pos()[1]<=308:
                    tela_inicial = False
                    game = True  
                    jogo = 1
                elif pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=322 and pygame.mouse.get_pos()[1]<=375:
                    tela_inicial = False
                    game = True
                    jogo = 2
                #elif pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=391 and pygame.mouse.get_pos()[1]<=449:
                    #tela_inicial = False
                    #game = True
#WIDTH = 1000
#HEIGHT = 550
    pygame.display.update()

#Verifica se são 2 jogadores
if jogo == 2:
    all_sprites.add(player2)  

# ===== Loop principal =====
while game==True:

    if VIDAS > 0:
        tempo.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            ########Teclas jogador 1#########
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
            
            #############Teclas jogador 2##############
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_a:
                    player2.speedx -= 8
                if event.key == pygame.K_d:
                    player2.speedx += 8
                if event.key == pygame.K_w:
                    player2.jump()
                if event.key == pygame.K_q:
                    player2.shoot()
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    player2.speedx = 0

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

    if VIDAS < 1:
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(gameover, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                        
    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados