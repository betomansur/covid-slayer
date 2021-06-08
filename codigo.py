import pygame
#from pygame import mixer
import random

pygame.init()
##Os nomes das variáveis está em uma mistura de português e inglês##

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 550
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Covid Slayer')

# ----- Inicia assets
#assets jogador
jog_img = pygame.image.load('Sprites/gunman.png').convert_alpha()
jog_img = pygame.transform.scale(jog_img, (90, 70))
#assets inimigo
inim_img = pygame.image.load('Sprites/bacteria1.png').convert_alpha()
inim_img = pygame.transform.scale(inim_img, (70, 70))
boss_img = pygame.image.load('Sprites/Boss1.png').convert_alpha()
boss_img = pygame.transform.scale(inim_img, (200, 200))
#assets background
bg = pygame.image.load("Sprites/hospital.jpg").convert()
background = pygame.transform.scale(bg, (1000, 550))
background_rect = background.get_rect()
#Tela de fim de jogo
go = pygame.image.load("Sprites/gameover.jpg").convert()
gameover = pygame.transform.scale(go, (1000, 550))
#Tela 2 de jogo
flo = pygame.image.load('Sprites/floresta.jpg').convert()
floresta = pygame.transform.scale(flo, (1000, 550))
#assets do tiro
bullet_img = pygame.image.load('Sprites/seringa.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (50, 20))
###FONTE DE TEXTO QUE O ANDREW TINHA DISPONIBILIZADO###
#assets fonte de texto
score_font = pygame.font.Font('font/PressStart2P.ttf', 28)

##########EXTRAS###########
# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
# Define valores iniciais
GRAVITY = 6
PONTOS = 0 
VIDAS = 15
VIDAS2= 0
VIDAS_BOSS = 5
###########################

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
        self.tiro = bullet_img
        self.lado = 1
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
        #Se estiver correndo para a direita
        if self.speedx > 0:
            self.image = pygame.image.load('Sprites/gunman.png').convert_alpha()
            self.lado = 1
        #Se estiver correndo para a esquerda
        if self.speedx < 0:
            self.image = pygame.image.load('Sprites/gunman_invertido.png').convert_alpha()
            self.lado = -1
        self.image = pygame.transform.scale(self.image, (90, 70))

    #Método que faz o personagem pular
    def jump(self):
        #Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 50
            self.state = JUMPING    
    #Função do tiro
    def shoot(self):
        if self.lado == 1:
            self.tiro = pygame.image.load('Sprites/seringa.png').convert_alpha()
            self.tiro = pygame.transform.scale(self.tiro, (50, 20))
            new_bullet = Bullet(self.tiro, self.rect.y+40, self.rect.x+70, 20)
        elif self.lado == -1:
            self.tiro = pygame.image.load('Sprites/seringa_invertida.png').convert_alpha()
            self.tiro = pygame.transform.scale(self.tiro, (50, 20))
            new_bullet = Bullet(self.tiro, self.rect.y+35, self.rect.x, -20)
        #A seringa será criada saindo da arma do jogador
        self.bullets.add(new_bullet)
        self.sprites.add(new_bullet)

#Classe do jogador 2
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
        self.lado = 1
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
        #Se estiver correndo para a direita
        if self.speedx > 0:
            self.image = pygame.image.load('Sprites/gunman.png').convert_alpha()
            self.lado = 1
        #Se estiver correndo para a esquerda
        if self.speedx < 0:
            self.image = pygame.image.load('Sprites/gunman_invertido.png').convert_alpha()
            self.lado = -1
        self.image = pygame.transform.scale(self.image, (90, 70))
        
    #Método que faz o personagem pular
    def jump(self):
        #Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 50
            self.state = JUMPING    
    #Função do tiro
    def shoot(self):
        if self.lado == 1:
            self.tiro = pygame.image.load('Sprites/seringa.png').convert_alpha()
            self.tiro = pygame.transform.scale(self.tiro, (50, 20))
            new_bullet = Bullet(self.tiro, self.rect.y+40, self.rect.x+70, 20)
        elif self.lado == -1:
            self.tiro = pygame.image.load('Sprites/seringa_invertida.png').convert_alpha()
            self.tiro = pygame.transform.scale(self.tiro, (50, 20))
            new_bullet = Bullet(self.tiro, self.rect.y+35, self.rect.x, -20)
        #A seringa será criada saindo da arma do jogador
        self.bullets.add(new_bullet)
        self.sprites.add(new_bullet)


#Classe do inimigo
class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        pygame.sprite.Sprite.__init__(self)
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([10, WIDTH-10])
        if self.rect.x == 10:
            self.lado = 'esq'
        if self.rect.x == WIDTH-10:
            self.lado = 'dir'
        self.rect.y = random.randint(HEIGHT-200, HEIGHT-40)
        self.speedx = random.randint(3, 4)
    #inimigo se move
    def update(self):
        if self.lado == 'esq':
            self.rect.x += self.speedx
        if self.lado == 'dir':
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH+10:
            self.lado = 'dir'
        if self.rect.left < -10:
            self.lado = 'esq'
        
class boss(pygame.sprite.Sprite):
    def __init__(self, boss_img, VIDAS_BOSS):
        pygame.sprite.Sprite.__init__(self)
        # Define estado atual
        self.image = boss_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-20
        self.rect.y = HEIGHT-20
        self.vidas = VIDAS_BOSS
    def update(self):
        if self.vidas < 1:
            self.kill()
          
#Classe do tiro
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.nem
    def __init__(self, tiro_img, bottom, centerx, speedx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.rect = self.image.get_rect()
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = speedx
    def update(self):
        if self.speedx>0:
            self.image = pygame.image.load('Sprites/seringa.png').convert_alpha()
        elif self.speedx<0:
            self.image = pygame.image.load('Sprites/seringa_invertida.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect.x += self.speedx
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()

#########################################################################
game = True
#Cria um relógio que conta o tempo em jogo
tempo = pygame.time.Clock()
FPS = 20

#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
collide_enemy = pygame.sprite.Group()
  
# Criando o jogador e inimigo
player = jogador(jog_img, VIDAS)
player2 = jogador2(jog_img, VIDAS2)
inimigo2 = boss(boss_img,VIDAS_BOSS)
all_sprites.add(player)
for i in range(0,5):
    enemy = inimigo(inim_img)
    all_sprites.add(enemy) 
    collide_enemy.add(enemy)

#------ Tela de inicio
tela_inicial = True
tela_credito = False
game = False
tela_boss = False
jogo=1
while tela_inicial:
    window.blit(background, (0, 0))
    #(janela, (cor,cor,cor), [eixox, eixoy, raio, grossura])
    pygame.draw.rect(window, (0,0,0), [335, 250, 350, 60]) 
    pygame.draw.rect(window, (0,0,0), [335, 320, 350, 60])
    pygame.draw.rect(window, (0,0,0), [335, 390, 350, 60])
    #Desenha nome do jogo
    text_nome = score_font.render("Covid Slay", True, (255, 0, 0))
    text_nome_rect = text_nome.get_rect()
    text_nome_rect.midtop = (500,  160)
    window.blit(text_nome, text_nome_rect)
    #Opção 1 jogador
    text_jog1 = score_font.render("1 Jogador", True, (255, 0, 0))
    text_jog1_rect = text_jog1.get_rect()
    text_jog1_rect.midtop = (510,  270)
    window.blit(text_jog1, text_jog1_rect)
    #Opção 2 jogadores
    text_jog2 = score_font.render("2 Jogadores", True, (255, 0, 0))
    text_jog2_rect = text_jog2.get_rect()
    text_jog2_rect.midtop = (510,  340)
    window.blit(text_jog2, text_jog2_rect)
    #Créditos 
    text_cred = score_font.render("Créditos", True, (255, 0, 0))
    text_cred_rect = text_cred.get_rect()
    text_cred_rect.midtop = (510,  410)
    window.blit(text_cred, text_cred_rect)
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                tela_inicial = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if pygame.mouse.get_pressed():
                #Caso aperte 1 jogador
                if pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=251 and pygame.mouse.get_pos()[1]<=308:
                    tela_inicial = False
                    game = True  
                    jogo = 1
                #Caso aperte 2 jogadores
                elif pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=322 and pygame.mouse.get_pos()[1]<=375:
                    tela_inicial = False
                    game = True
                    jogo = 2
                #Caso aperte créditos
                elif pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=391 and pygame.mouse.get_pos()[1]<=449:
                    tela_credito = True
    
    while tela_credito == True:
        window.blit(background, (0, 0))
        pygame.draw.rect(window, (0,0,0), [20, 30, 350, 60])
        text_back = score_font.render("Voltar", True, (255, 0, 0))
        text_back_rect = text_back.get_rect()
        text_back_rect.midtop = (500,  160)
        window.blit(text_back, text_back_rect) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    tela_inicial = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pygame.mouse.get_pressed():
                    #Caso aperte 1 jogador
                    print(pygame.mouse.get_pos())
                    if pygame.mouse.get_pos()[0]>=200 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=251 and pygame.mouse.get_pos()[1]<=308:
                        tela_credito = False


    pygame.display.update()

#Verifica se são 2 jogadores
if jogo == 2:
    VIDAS2 = 3
    all_sprites.add(player2)

# ===== Loop principal =====
while game==True:
    if VIDAS > 0 or VIDAS2 > 0:
        tempo.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            ########Teclas jogador 1#########
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
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

            if jogo ==2:
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

        #Colisões
        hits_jog1 = pygame.sprite.spritecollide(player, collide_enemy, True)
        hit_tiro = pygame.sprite.groupcollide(all_bullets, collide_enemy, True, True)

        if len(collide_enemy) < 7:
            en = inimigo(inim_img)
            all_sprites.add(en)
            collide_enemy.add(en)
        for hit in hits_jog1:
            VIDAS -= 1
        for hit in hit_tiro:
            PONTOS+=10
        if jogo == 2:
            hits_jog2 = pygame.sprite.spritecollide(player2, collide_enemy, True)
            if len(hits_jog2) > 0:
                VIDAS2 -= 1

        #Atualiza sprites
        all_sprites.update()
        collide_enemy.update()

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor preto
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

        if jogo == 2:
            text_surface2 = score_font.render(chr(9829) * VIDAS2, True, (255, 0, 0))
            text_rect2 = text_surface.get_rect()
            text_rect2.bottomleft = (WIDTH -100, HEIGHT - 10)
            window.blit(text_surface2, text_rect2)
    
    #Verifica se o jogo acabou
    if jogo == 1:
        if VIDAS<1:
            window.fill((0, 0, 0))  # Preenche com a cor preto
            window.blit(gameover, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = False
    else:
        if VIDAS<1:
            all_sprites.remove(player)
        elif VIDAS2<1:
            all_sprites.remove(player2)
        if VIDAS<1 and VIDAS2<1:
            window.fill((0, 0, 0))  # Preenche com a cor preto
            window.blit(gameover, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = False

    if PONTOS == 10000:
        game = False
        tela_boss = True
    pygame.display.update()  # Mostra o novo frame para o jogador
while tela_boss:
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(floresta, (0, 0))
    all_sprites.add(inimigo2)
    collide_enemy.add(inimigo2)
    if len(hit_tiro) > 0:
        VIDAS_BOSS-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    all_sprites.update()
    collide_enemy.update()
    all_sprites.draw(window)
                
    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados