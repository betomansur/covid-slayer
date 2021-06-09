from typing import ValuesView
import pygame
#from pygame import mixer
import random

from pygame import mixer



pygame.init()
##Os nomes das variáveis está em uma mistura de português e inglês##



#musica
mixer.music.load('Sprites/music.wav')
mixer.music.play(-1)
#mixer.music.load('Sprites/earape.wav')
#mixer.music.play(-1)


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
boss_img = pygame.transform.scale(boss_img, (90, 90))
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
VIDAS = 5
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
    def __init__(self, inim_img, speedx):
        pygame.sprite.Sprite.__init__(self)
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([0, WIDTH])
        if self.rect.x == 0:
            self.lado = 'esq'
        if self.rect.x == WIDTH:
            self.lado = 'dir'
        self.rect.y = random.randint(HEIGHT-200, HEIGHT-40)
        self.speedx = speedx
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
        self.rect.x = WIDTH-200
        self.rect.y = HEIGHT-100
        self.vidas = VIDAS_BOSS
        self.bacteria = inim_img
        self.collide_enemy = collide_enemy
        self.sprites = all_sprites
        self.time = 5000
    def update(self):
        self.time -= 50
        new_bacteria = inimigo(self.bacteria, 3)
        if len(self.collide_enemy)<3:
            self.collide_enemy.add(new_bacteria)
            self.sprites.add(new_bacteria)
          
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
FPS = 30
#------ Tela de inicio
tela_inicial = True
tela_credito = False
game = False
tela_jogo = False
tela_boss = False
tela_vitoria = False
#Tela de inicio
while tela_inicial:
    window.blit(background, (0, 0))
    #(janela, (cor,cor,cor), [x, y, largura x, largura y])
    pygame.draw.rect(window, (0,0,0), [335, 250, 350, 60]) 
    pygame.draw.rect(window, (0,0,0), [335, 320, 350, 60])
    pygame.draw.rect(window, (0,0,0), [335, 390, 350, 60])
    #Desenha nome do jogo
    text_nome = score_font.render("Covid Slay", True, (0, 0, 0))
    window.blit(text_nome, (365,160))
    #Desenha Opção de 1 jogador
    text_jog1 = score_font.render("1 Jogador", True, (255, 0, 0))
    window.blit(text_jog1, (380, 270))
    #Desenha Opção de 2 jogadores
    text_jog2 = score_font.render("2 Jogadores", True, (255, 0, 0))
    window.blit(text_jog2, (360, 340))
    #Desenha Créditos 
    text_cred = score_font.render("Créditos", True, (255, 0, 0))
    window.blit(text_cred, (400, 410))
    #Verifica se apertou algum botão
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                tela_inicial = False
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if pygame.mouse.get_pressed():
                #Caso aperte 1 jogador
                if pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=251 and pygame.mouse.get_pos()[1]<=308:
                    tela_inicial = False
                    game = True 
                    tela_jogo= True
                    jogo = 1
                #Caso aperte 2 jogadores
                elif pygame.mouse.get_pos()[0]>=334 and pygame.mouse.get_pos()[0]<=683 and pygame.mouse.get_pos()[1]>=322 and pygame.mouse.get_pos()[1]<=375:
                    tela_inicial = False
                    game = True
                    tela_jogo = True
                    jogo = 2
                #Caso aperte créditos
                elif pygame.mouse.get_pos()[0]>=336 and pygame.mouse.get_pos()[0]<=684 and pygame.mouse.get_pos()[1]>=395 and pygame.mouse.get_pos()[1]<=450:
                    tela_credito = True
    
    #Tela de créditos
    while tela_credito == True:
        window.blit(background, (0, 0))
        #Cria retângulos
        pygame.draw.rect(window, (0,0,0), [20, 30, 240, 60])
        pygame.draw.rect(window, (0,0,0), [200, 180, 585, 200])
        #Desenha opção de voltar
        text_back = score_font.render("Voltar", True, (255, 0, 0))
        window.blit(text_back, (60,50)) 
        #Desenha nome dos criadores
        text_gui = score_font.render("Guillermo Kuznietz", True, (200,25, 100))
        text_ray = score_font.render("Raymond Joseph Diwan", True, (100, 25, 75))
        text_beto = score_font.render("Alberto Mansur", True, (100, 190, 60))
        window.blit(text_gui, (215, 200))
        window.blit(text_ray, (215, 260))
        window.blit(text_beto,(215, 320))

        #Verifica se apertou algum botão
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    tela_inicial = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if pygame.mouse.get_pressed():
                    if pygame.mouse.get_pos()[0]>=10 and pygame.mouse.get_pos()[0]<=370 and pygame.mouse.get_pos()[1]>=30 and pygame.mouse.get_pos()[1]<=90:
                        tela_credito = False
        pygame.display.update()
    pygame.display.update()

#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
collide_enemy = pygame.sprite.Group()
all_boss = pygame.sprite.Group()
# Criando os jogadores e inimigos
if jogo == 1:
    VIDAS += 4
player = jogador(jog_img, VIDAS)
player2 = jogador2(jog_img, VIDAS2)
inimigo2 = boss(boss_img,VIDAS_BOSS)
#Adiciona jogadores e inimigos nos grupos
all_boss.add(inimigo2)
all_sprites.add(player)
for i in range(5):
    if jogo == 1:
        enemy = inimigo(inim_img, 2)
    elif jogo==2:
        enemy = inimigo(inim_img, 2.6)
        VIDAS2 = 5
        all_sprites.add(player2)
    all_sprites.add(enemy) 
    collide_enemy.add(enemy)


while game:
    if VIDAS > 0 or VIDAS2 > 0:
        tempo.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            ########Teclas jogador 1#########
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if VIDAS > 0:
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

            if jogo ==2 and VIDAS2>0:
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
        hits_jog2 = pygame.sprite.spritecollide(player2, collide_enemy, True)
        hit_bala_boss = pygame.sprite.spritecollide(inimigo2, all_bullets, True)
        hit_tiro = pygame.sprite.groupcollide(all_bullets, collide_enemy, True, True)

        for hit in hits_jog1:
            VIDAS -= 1
        for hit in hit_tiro: 
            PONTOS+=10
        if jogo == 2:
            if len(hits_jog2) > 0:
                VIDAS2 -= 1

            tela_jogo = False
            tela_boss = True
            all_sprites.empty()
            collide_enemy.empty()
            all_sprites.add(player)
            all_sprites.add(inimigo2)
            if jogo==2:
                all_sprites.add(player2)
            x-=1

        if tela_jogo == True:
            if len(collide_enemy) < 7:
                if jogo == 1:
                    en = inimigo(inim_img, 2)
                elif jogo == 2:
                    en = inimigo(inim_img, 2.6)
                all_sprites.add(en)
                collide_enemy.add(en)
            #Atualiza sprites
            all_sprites.update()
            collide_enemy.update()
            # ----- Gera saídas
            window.fill((0, 0, 0))  # Preenche com a cor preto
            window.blit(background, (0, 0))
            # Desenhando as sprites
            all_sprites.draw(window)

        if tela_boss == True:
            hit_tiro = pygame.sprite.groupcollide(all_bullets, collide_enemy, False, True)
            if len(collide_enemy)<3:
                all_sprites.add(en)
            if jogo == 2:
                if len(hit_joga2_boss) > 0:
                    VIDAS2 -=1
            if len(hit_bala_boss) > 0:
                VIDAS_BOSS-=1
            if len(hit_joga_boss) > 0:
                VIDAS -=1
            if VIDAS_BOSS < 1:
                tela_boss = False
                tela_vitoria = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            all_sprites.update()
            collide_enemy.update()
            window.fill((0, 0, 0))  # Preenche com a cor preto
            window.blit(floresta, (0, 0))
            all_sprites.draw(window)
        
        if tela_vitoria == True: 
            game = False



        # Desenhando o score
        text_surface = score_font.render("{:06d}".format(PONTOS), True, (255, 0, 200))
        window.blit(text_surface, (15, 20))

        # Desenhando as vidas
        if jogo == 1:
            text_vida = score_font.render(chr(9829) * VIDAS, True, (255, 0, 0))
        elif jogo == 2:
            text_vida = score_font.render('P1'+chr(9829) * VIDAS, True, (255, 0, 0))
            text_vida2 = score_font.render('P2'+chr(9829) * VIDAS2, True, (255, 0, 0))
            window.blit(text_vida2, (WIDTH-200, HEIGHT - 40))
        window.blit(text_vida, (15, HEIGHT - 40))
    
    #Verifica se o jogo acabou
    if jogo == 1:
        if VIDAS<1:
            window.fill((0, 0, 0))  # Preenche com a cor preto
            window.blit(gameover, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

    elif jogo == 2:
        if VIDAS<1:
            all_sprites.remove(player)
            hits_jog1 = pygame.sprite.spritecollide(player, collide_enemy, False)
        elif VIDAS2<1:
            all_sprites.remove(player2)
            hits_jog2 = pygame.sprite.spritecollide(player2, collide_enemy, False)
        if VIDAS<1 and VIDAS2<1:
            window.fill((0, 0, 0))  # Preenche com a cor preto
            window.blit(gameover, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                
    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados