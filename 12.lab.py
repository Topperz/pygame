__author__ = 'Topper121'

"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from random import randrange
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rectangle:
    def __init__(self, color, x, y, width, height, change_x, change_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])


    def move(self):
        self.x += self.change_x
        self.y += self.change_y

class Ellipse(Rectangle):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.width, self.height], 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

my_list = []
for i in range(100):
    my_object = Rectangle((randrange(255),randrange(255),randrange(255)), randrange(600),randrange(400), randrange(20,70), randrange(20,70), randrange(-3,3), randrange(-3,3))
    my_list.append(my_object)

for i in range(50):
    my_object = Ellipse((randrange(255),randrange(255),randrange(255)), randrange(600),randrange(400), randrange(20,70), randrange(20,70), randrange(-3,3), randrange(-3,3))
    my_list.append(my_object)

print(my_list)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #pygame.draw.rect(screen, GREEN, [450, 350, 50, 50])

    for item in my_list:
        item.draw(screen)
        if item.x <= 0 or (item.x + item.width) >= 700:
            item.change_x *= -1
        if item.y <= 0 or item.y + item.height >= 500 :
            item.change_y *= -1

        item.move()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()