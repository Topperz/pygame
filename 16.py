__author__ = 'Topper121'

"""

"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Variables

width = 20
height = 20
margin = 5


#font = pygame.font.SysFont("serif", 25)
#text = font.render("Click", True, BLACK)
#x = 0
#y = 0
# --- Create grid of numbers
# Create an empty list
gamesize = int(input("Game size: "))

grid = []
# Loop for each row
for row in range(gamesize):
    # For each row, create a list that will
    # represent an entire row
    grid.append([])
    # Loop for each column
    for column in range(gamesize):
        # Add a the number zero to the current row
        grid[row].append(random.randrange(-1,2,2))

#grid[1][5] = 1

for line in grid:
    print(line)
# Set the width and height of the screen [width, height]
screensize = int(25.5 * gamesize)
size = (screensize, screensize)
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            y = mouse_position[1]
            x = mouse_position[0]
            k = (y - 3) // (height + margin)
            j = (x - 2) // (width + margin)

            # Handling corner cases
            if j <= 0 and k <= 0:
                j = 0
                k = 0
                grid[k][j] *= -1
                grid[k+1][j] *= -1
                grid[k][j+1] *= -1
            elif j >= (gamesize - 1) and k <= 0:
                j = (gamesize - 1)
                k = 0
                grid[k][j] *= -1
                grid[k][j-1] *= -1
                grid[k+1][j] *= -1
            elif j >= (gamesize - 1) and k >= (gamesize - 1):
                j = (gamesize - 1)
                k = (gamesize - 1)
                grid[k][j] *= -1
                grid[k-1][j] *= -1
                grid[k][j-1] *= -1
            elif j <= 0 and k >= (gamesize - 1):
                j = 0
                k = (gamesize - 1)
                grid[k][j] *= -1
                grid[k-1][j] *= -1
                grid[k][j+1] *= -1
            #Handling edge of grid
            elif j >= (gamesize - 1):
                j = (gamesize - 1)
                grid[k][j] *= -1
                grid[k+1][j] *= -1
                grid[k-1][j] *= -1
                grid[k][j-1] *= -1
            elif k >= (gamesize - 1):
                k = (gamesize - 1)
                grid[k][j] *= -1
                grid[k-1][j] *= -1
                grid[k][j+1] *= -1
                grid[k][j-1] *= -1
            elif j <= 0:
                j = 0
                grid[k][j] *= -1
                grid[k+1][j] *= -1
                grid[k-1][j] *= -1
                grid[k][j+1] *= -1
            elif k <= 0:
                k = 0
                grid[k][j] *= -1
                grid[k+1][j] *= -1
                grid[k][j+1] *= -1
                grid[k][j-1] *= -1
            #Handling rest of grid
            else:
                grid[k][j] *= -1
                grid[k+1][j] *= -1
                grid[k-1][j] *= -1
                grid[k][j+1] *= -1
                grid[k][j-1] *= -1



    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    for column in range(gamesize):
        for row in range(gamesize):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [margin + 0 + column * (width + margin), margin + 0 + row * (height + margin), width, height],0)

    #screen.blit(text, [x, y])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()