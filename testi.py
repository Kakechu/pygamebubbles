import pygame
import sys
from pygame.locals import *
pygame.init()


#screen
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Oma peli")


level = pygame.Surface((900,600))
backgroundColor = (213, 242, 250)
level.fill(backgroundColor)

#hand (character)
hand = pygame.image.load("hand.png").convert_alpha()
hand_speed = 1
handArea = hand.get_rect()
handArea.left = 300
handArea.top = 300


#set boundaries
left_wall = pygame.Rect(-1, 0, 1, screen_height) #left, top, width, height
right_wall = pygame.Rect(screen_width+1, 0, 1, screen_height)
ceiling = pygame.Rect(-1, -1, screen_width+2, 1)
floor = pygame.Rect(-1, screen_height+1, screen_width+2, 1)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(level, (0,0))
    screen.blit(hand, (300, 300))
    #pygame.display.flip()

    keypressed = pygame.key.get_pressed()

    
    if keypressed[K_LEFT] and not handArea.colliderect(left_wall):
        handArea.move_ip((-hand_speed,0))
    if keypressed[K_RIGHT] and not handArea.colliderect(right_wall):
        handArea.move_ip((hand_speed,0))
    if keypressed[K_DOWN] and not handArea.colliderect(floor):
        handArea.move_ip((0,hand_speed))
    if keypressed[K_UP] and not handArea.colliderect(ceiling):
        handArea.move_ip((0,-hand_speed))

    screen.blit(level, (0,0))
    screen.blit(hand, handArea)
    pygame.display.flip()

    