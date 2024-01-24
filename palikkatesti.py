import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Avoid Collision Game")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)

# Define the MyObject class
class MyObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed_x, speed_y):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self):
        pygame.draw.rect(screen, red, self.rect)

# Create instances of MyObject with different speeds
object1 = MyObject(100, 100, 50, 50, 2, 1)
object2 = MyObject(200, 200, 50, 50, -1, -2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the positions of the objects
    object1.move()
    object2.move()

    # Check for collisions
    if object1.rect.colliderect(object2.rect):
        print("Game Over - Collision Detected!")
        pygame.quit()
        sys.exit()

    # Bounce off the edges of the window
    if object1.rect.left < 0 or object1.rect.right > width:
        object1.speed_x = -object1.speed_x

    if object1.rect.top < 0 or object1.rect.bottom > height:
        object1.speed_y = -object1.speed_y

    if object2.rect.left < 0 or object2.rect.right > width:
        object2.speed_x = -object2.speed_x

    if object2.rect.top < 0 or object2.rect.bottom > height:
        object2.speed_y = -object2.speed_y

    # Update the screen
    screen.fill(white)

    # Draw the objects
    object1.draw()
    object2.draw()

    # Update the display
    pygame.display.flip()