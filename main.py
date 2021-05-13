import pygame

#Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('sp_icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('space_ship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    #RGB - Red Green Blue
    screen.fill((0, 0, 0))
    print(playerX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")

    player(playerX, playerY)
    pygame.display.update()