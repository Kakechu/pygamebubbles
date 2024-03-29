import pygame
import sys
from pygame.locals import *
pygame.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#create boundaries for the screen
left_wall = pygame.Rect(-1, 0, 1, screen_height) #left, top, width, height
right_wall = pygame.Rect(screen_width+1, 0, 1, screen_height)
ceiling = pygame.Rect(-1, -1, screen_width+2, 1)
floor = pygame.Rect(-1, screen_height+1, screen_width+2, 1)


#button images
play_button_img = pygame.image.load("play_button.png")
quit_button_img = pygame.image.load("quit_button.png")
welcome_text = pygame.image.load("welcome.png")
play_again_img = pygame.image.load("play_again_button.png")
game_over_text = pygame.image.load("game_over.png")

#button coordinates into variables
welcome_x = screen_width/2 - 250
welcome_y = 50
button_x = screen_width/2 - 200
upper_button_y = screen_height/2 - 75
lower_button_y = screen_height/2 + 75

#object images
bubble = pygame.image.load("kupla.png").convert_alpha() #size:100x90
hand = pygame.image.load("hand.png").convert_alpha()
handArea = hand.get_rect()

class Button(): 
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            #print("hover")
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                #print("Clicked")

        if pygame.mouse.get_pressed()[0] == 0: #not clicked
            self.clicked = False


        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

#create button instances
play_button = Button(button_x, upper_button_y, play_button_img)
quit_button = Button(button_x, lower_button_y, quit_button_img)
play_again_button = Button(button_x, upper_button_y, play_again_img)


#create class for bubble
class Bubble():
    def __init__(self, x, y, image, speed):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = speed

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        self.rect.move_ip(self.speed)
        if self.rect.colliderect(left_wall) or self.rect.colliderect(right_wall):
            self.speed[0] = -self.speed[0]

        if self.rect.colliderect(ceiling) or self.rect.colliderect(floor):
            self.speed[1] = -self.speed[1]

        if self.rect.colliderect(handArea):
            self.speed[0] = -self.speed[0]
            self.speed[1] = -self.speed[1]


def start_menu():


    pygame.display.set_caption("Welcome")
    menu = pygame.Surface((screen_width, screen_height))
    menu_background_color = (52, 78, 91)
    menu.fill(menu_background_color)

    not_selected = True
    while not_selected:
    
        #event handler
        for event in pygame.event.get():
            if play_button.draw():
                play()

            if quit_button.draw():
                pygame.quit()
                sys.exit()

            #quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(menu, (0,0))
        screen.blit(welcome_text, (welcome_x, welcome_y))
        play_button.draw()
        quit_button.draw()
        pygame.display.flip()

def game_over_menu():
    pygame.display.set_caption("Game Over")
    menu = pygame.Surface((screen_width, screen_height))
    menu_background_color = (52, 78, 91)
    menu.fill(menu_background_color)

    not_selected = True
    while not_selected:

        #event handler
        for event in pygame.event.get():
            if play_again_button.draw():
                play()

            if quit_button.draw():
                pygame.quit()
                sys.exit()

            #quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(menu, (0,0))
        screen.blit(game_over_text, (button_x, welcome_y))
        play_again_button.draw()
        quit_button.draw()
        pygame.display.flip()

def play():

    #screen
    pygame.display.set_caption("Let's play")
    level = pygame.Surface((screen_width, screen_height))
    backgroundColor = (213, 242, 250)
    level.fill(backgroundColor)

    #define hand speed and start position
    hand_speed = 1
    handArea.left = 400
    handArea.top = 400

    #create bubble instance
    bubble_1 = Bubble(500, 500, bubble, [1,1])
    bubble_2 = Bubble(0, 0, bubble, [1,1])

    #game loop
    run = True
    while run:
        pygame.time.delay(3)
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(level, (0,0))
        screen.blit(hand, handArea)

        bubble_1.draw()
        bubble_2.draw()
        pygame.display.flip()

        if bubble_1.rect.colliderect(bubble_2.rect):
            game_over_menu()

        #define hand movements
        keypressed = pygame.key.get_pressed()
        
        if keypressed[K_LEFT] and not handArea.colliderect(left_wall):
            handArea.move_ip((-hand_speed,0))
        if keypressed[K_RIGHT] and not handArea.colliderect(right_wall):
            handArea.move_ip((hand_speed,0))
        if keypressed[K_DOWN] and not handArea.colliderect(floor):
            handArea.move_ip((0,hand_speed))
        if keypressed[K_UP] and not handArea.colliderect(ceiling):
            handArea.move_ip((0,-hand_speed))

start_menu()
