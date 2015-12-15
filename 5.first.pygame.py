"""
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import time
import math
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.141592653
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
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
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, RED, [100, 100, 100, 100])
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.line(screen, GREEN, [200, 100], [300, 0], 5)
    pygame.draw.line(screen, GREEN, [100, 200], [0, 300], 5)
    pygame.draw.line(screen, GREEN, [200, 200], [300, 300], 5)

    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
        #pygame.display.flip()
        #time.sleep(1)
    #for i in range(200):
 #
  #      radians_x = i / 20
   #     radians_y = i / 6
 #
  #      x = int( 75 * math.sin(radians_x)) + 200
   #     y = int( 75 * math.cos(radians_y)) + 200
 #
  #      pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)
        #pygame.display.flip()
        #time.sleep(0.1)

    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    #pygame.draw.arc(screen, GREEN, [100,100,250,200],  PI,     PI/2, 2)
    #pygame.draw.arc(screen, BLACK, [100,100,250,200],     0,   PI/2, 2)
    #pygame.draw.arc(screen, RED,   [100,100,250,200],3*PI/2,   2*PI, 2)
    #pygame.draw.arc(screen, BLUE,  [100,100,250,200],    PI, 3*PI/2, 2)

    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI/2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI/2 , PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, PI * 1.5, 2)
    pygame.draw.arc(screen, RED, [20, 220, 250, 200], PI * 1.5 , PI * 2, 2)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
