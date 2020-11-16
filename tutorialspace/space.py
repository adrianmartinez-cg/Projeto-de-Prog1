import pygame
import random

#Inicializando o pygame e criando a janela com titulo e icone
pygame.init() 
screen=pygame.display.set_mode([800,600]) 
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("space/ufo.png")
pygame.display.set_icon(icon)

#Imagem de fundo
background=pygame.image.load('space/background.png')

# Jogador
playerImg=pygame.image.load('space/player.png')
playerX=370
playerY=480
playerX_change=0

# Inimigo
enemyImg=pygame.image.load('space/enemy1.png')
enemyX=random.randint(0,700)
enemyY=random.randint(50,150)
enemyX_change=2
enemyY_change=40

def player(x,y):
    screen.blit(playerImg,(x,y)) #desenha a imagem do player na tela
def enemy(x,y):
    screen.blit(enemyImg,(x,y)) 

gameLoop=True # Variavel booleana para deixar o jogo rodando
while gameLoop:
    screen.fill([0,0,0]) #preenche a tela com alguma cor
    screen.blit(background,(0,0))
    for event in pygame.event.get(): # Aqui iremos ver os eventos que estão acontecendo
        if event.type == pygame.QUIT: # Se for o botao de fechar
            gameLoop=False
        if event.type == pygame.KEYDOWN: # se alguma tecla foi pressionada (keyup = soltar tecla)
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            elif event.key == pygame.K_RIGHT:
                playerX_change= 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
    
    playerX+= playerX_change
    if playerX <= 0: # Para nao sair da janela do jogo
        playerX=0
    elif playerX >= 736:
        playerX=736
    
    enemyX+= enemyX_change
    if enemyX <= 0:
        enemyX_change=2
        enemyY+= enemyY_change
    elif enemyX >= 736:
        enemyX_change=-2
        enemyY+= enemyY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update() #mantem a janela do jogo aberta

