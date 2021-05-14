import pygame
import random
import math

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

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(20)

#Laser
#"ready" - not possible to see the laser on the screen
#"fire" - the laser is currently moving

laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state = "ready"

score = 0


def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_laser(x, y):
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 16, y + 10))

#Disntance between two points and the midpoint
def isCollision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt((math.pow(enemyX-laserX, 2)) + (math.pow(enemyY-laserY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    #RGB - Red Green Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    # it is for getting the actual coordinate (X) of the spaceship
                    laserX = playerX
                    fire_laser(laserX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #5 = 5 + -0.1 -> 5 = 5 -0.1
    #5 = 5 + 0.1

    #check for boundaries (so it won't go out of bounds)
    #736 = 800px - 64px (spaceship size)
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy Movement in the boundaries
    for i in range (num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX[i] = -0.4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            laserY = 480
            laser_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #Laser Movement
    if laserY <= 0:
        laserY = 480
        laser_state = "ready"

    if laser_state == "fire":
        fire_laser(playerX, laserY)
        laserY -= laserY_change


    player(playerX, playerY)

    pygame.display.update()