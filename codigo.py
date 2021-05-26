import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 550
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Covid Slay')


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
bg = pygame.image.load("Sprites/hospital2.png.jpg")
#background = pygame.image.load('sprite do fundo').convert()
background = pygame.transform.scale(bg, (700, 620))
background_rect = background.get_rect()
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
    
    def update(self):

        #Movimentação em y
        self.speedy += GRAVITY
        #Atualiza a posição y
        self.rect.y += self.speedy
        #Atualiza a posição x
        self.rect.x += self.speedx

        #Se jogador colidiu com algum inimigo
        #collisions = pygame.sprite.spritecollide(self, inimigo, False)
        #Perde uma vida
        #for collision in collisions:
            #self.lifes -= 1
        
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


    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bullet = Bullet(self.kisspng-syringe-injection-vector-syringes.jpg, self.rect.top, self.rect.centerx)
        self.all_sprites.add(new_bullet)
        self.all_bullets.add(new_bullet)

class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100, HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTHR_WIDTH)
            self.rect.y = random.randint(-100, HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()


#Classe do inimigo
class inimigo(pygame.sprite.Sprite):
    def __init__(self, inim_img):
        pygame.sprite.Sprite.__init__(self)
        
        # Define estado atual
        self.image = inim_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 200
        self.speedx = 0
        self.speedy = 0
    
    #inimigo se move
    def update(self):
        self.rect.x += 4
        if self.rect.left > WIDTH:
            self.rect.right = -100   

class Plataforma (pygame.sprite.Sprite):
    def __init__(self,chao_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = chao_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = HEIGHT-10


game = True
#Cria um relógio que conta o tempo em jogo
tempo = pygame.time.Clock()
FPS = 20

#############COLISõES#############
#Cria grupos com as sprites e collides
all_sprites = pygame.sprite.Group()
collide_enemy = pygame.sprite.Group()
collide_gema = pygame.sprite.Group()
collide_meteoros = pygame.sprite.Group()
# Criando o jogador, inimigo e gemas
player = jogador(jog_img, VIDAS)
enemy = inimigo(inim_img)
chao = Plataforma(chao_img)
#Adicionando sprites em uma variável global
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(chao)
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
                elif event.key == pygame.K_UP:
                    player.jump()
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.speedx = 0

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

    pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados