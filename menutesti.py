import pygame
import sys
from pygame.locals import *
pygame.init()

#configuring the window
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#button images
play_button = pygame.image.load("play_button.png")
quit_button = pygame.image.load("quit_button.png")
welcome_text = pygame.image.load("welcome.png")
play_again_button = pygame.image.load("play_again_button.png")

#button coordinates into variables
welcome_x = screen_width/2 - 250
welcome_y = 50
button_x = screen_width/2 - 200
upper_button_y = screen_height/2 - 75
lower_button_y = screen_height/2 + 75

#create button class
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
        #print(pos)
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            #print("hover")
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                #print("CLICKED")
                #return True
                action = True


        if pygame.mouse.get_pressed()[0] == 0: #not clicked
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        #print(action)
        return action

#create button instances
play_button = Button(button_x, upper_button_y, play_button)
quit_button = Button(button_x, lower_button_y, quit_button)


#objects
bubble = pygame.image.load("kupla.png").convert_alpha()
hand = pygame.image.load("hand.png").convert_alpha()

        
class Bubble():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.collided = False

    #def draw(self):



def play():

    #screen

    pygame.display.set_caption("Let's play")


    level = pygame.Surface((screen_width, screen_height))
    backgroundColor = (213, 242, 250)
    level.fill(backgroundColor)

    #objects
    bubble = pygame.image.load("kupla.png").convert_alpha()
    bubble2 = pygame.image.load("kupla.png").convert_alpha()
    hand = pygame.image.load("hand.png").convert_alpha()

    bubbleArea = bubble.get_rect()
    bubble2Area = bubble2.get_rect()
    handArea = hand.get_rect()

    bubbleArea.left = 200
    bubbleArea.top = 200
    bubble2Area.left = 400
    bubble2Area.top = 100
    handArea.left = 300
    handArea.top = 300

    hand_speed = 1
    speed = [1, 1]

    #ympäröidään screen suorakulmiolla

    left_wall = pygame.Rect(-1, 0, 1, screen_height) #left, top, width, height
    right_wall = pygame.Rect(screen_width+1, 0, 1, screen_height)
    ceiling = pygame.Rect(-1, -1, screen_width+2, 1)
    floor = pygame.Rect(-1, screen_height+1, screen_width+2, 1)


    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        



        #bubbleArea.move_ip(speed)
        #bubble2Area.move_ip(speed)

        #pygame.draw.rect(screen, (255, 0,0), (500, 300, 100, 100))
        #pygame.display.flip()

        screen.blit(level, (0,0))
        screen.blit(bubble, bubbleArea)
        screen.blit(bubble2, bubble2Area)
        screen.blit(hand, handArea)

        #pygame.display.flip()

        #määritetään käden liikkeet
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
        screen.blit(bubble, bubbleArea)
        screen.blit(bubble2, bubble2Area)
        screen.blit(hand, handArea)
        pygame.display.flip()






not_selected = True
while not_selected:
    pygame.display.set_caption("Welcome")
    menu = pygame.Surface((screen_width, screen_height))
    menu_background_color = (52, 78, 91)
    menu.fill(menu_background_color)

    #if-lause äsken täällä


    #event handler
    for event in pygame.event.get():

        if play_button.draw():#en pääse tänne!!!

            #print("Start")
            play()

        if quit_button.draw():
            #print("Quit")
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

            #if event.type == MOUSEBUTTONDOWN
    screen.blit(menu, (0,0))
    screen.blit(welcome_text, (welcome_x, welcome_y))
    play_button.draw()
    quit_button.draw()
        
        #screen.blit(play_button, (button_x, upper_button_y))
        #screen.blit(quit_button, (button_x, lower_button_y))
    pygame.display.flip()
    




#start_menu()
#play()