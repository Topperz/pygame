__author__ = 'Topper121'

import pygame

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

pygame.display.set_caption("My Drawing")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Load picture

background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("player.png").convert()

click_sound = pygame.mixer.Sound("laser5.ogg")

legs_move_speed = 1

moved = 0

start_pos = 0
start_pos_y = 0
# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

leg_list_left = []
for i in range(0,400,100):
    x1 = 105 + i
    y1 = 200
    x2 = 105 + i
    y2 = 95
    leg_list_left.append(([x1,y1],[x2,y2]))

leg_list_right = []
for i in range(0,400,100):
    x1 = 105 + i
    y1 = 300
    x2 = 105 + i
    y2 = 405
    leg_list_right.append([[x1,y1],[x2,y2]])

feet_left = []
for i in range(0,400,100):
    x1 = 105 + i
    y1 = 80
    feet_left.append([x1,y1])

feet_right = []
for i in range(0,400,100):
    x1 = 105 + i
    y1 = 420
    feet_right.append([x1,y1])

print(leg_list_left[0][0][0])
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User press down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 0

        #User click mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()


    # Move the object according to the speed vector.
    start_pos = start_pos + x_speed
    start_pos_y = start_pos_y + y_speed

    # --- Game logic should go here

    # --- Drawing code should go here


    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    screen.blit(background_image, [0, 0])

    #Legs
    #for x_offset in range(0,400,100):
        #pygame.draw.line(screen, BLUE, [105 + x_offset, 200], (105 + x_offset, 100), 11)
        #pygame.draw.circle(screen, BLACK, (105 + x_offset + int(moved/2),80),20)
        #pygame.draw.rect(screen, RED, [100 + x_offset, 100, 10, 100])
        #pygame.draw.circle(screen, BLACK, (105 + x_offset + moved,420),20)
        #pygame.draw.rect(screen, RED, [100 + x_offset, 300, 10, 100])

    #draw the left legs
    for i in range(len(leg_list_left)):
        pygame.draw.line(screen, RED, [start_pos + leg_list_left[i][0][0], start_pos_y + leg_list_left[i][0][1]], [start_pos + leg_list_left[i][1][0], start_pos_y + leg_list_left[i][1][1]], 11)

    #draw the left feet
    for i in range(len(feet_left)):
        pygame.draw.circle(screen, BLACK, [start_pos + feet_left[i][0], start_pos_y + feet_left[i][1]], 20)

    #draw the right legs
    for i in range(len(leg_list_right)):
        pygame.draw.line(screen, RED, [start_pos + leg_list_right[i][0][0], start_pos_y + leg_list_right[i][0][1]], [start_pos + leg_list_right[i][1][0], start_pos_y + leg_list_right[i][1][1]], 11)

    #draw the right feet
    for i in range(len(feet_right)):
        pygame.draw.circle(screen, BLACK, [start_pos + feet_right[i][0], start_pos_y + feet_right[i][1]], 20)

    #keep legs moving back and forth
    if moved > 90 or moved < -90:
        legs_move_speed *= -1

    #move legs and feet
    for i in range(len(leg_list_left)):
        leg_list_left[i][1][0] += legs_move_speed
        leg_list_right[i][1][0] += legs_move_speed
        feet_left[i][0] += legs_move_speed
        feet_right[i][0] += legs_move_speed
        moved += legs_move_speed

    #Body
    pygame.draw.rect(screen, GREEN, [start_pos + 50, start_pos_y + 200, 500, 100])

    #Head
    pygame.draw.circle(screen, RED, (start_pos + 550, start_pos_y + 250), 65)
    pygame.draw.circle(screen, BLUE, (start_pos + 530, start_pos_y + 220), 10)
    pygame.draw.circle(screen, BLUE, (start_pos + 530, start_pos_y + 280), 10)
    pygame.draw.circle(screen, BLACK, (start_pos + 550, start_pos_y + 250), 5)
    pygame.draw.arc(screen, BLUE, [start_pos + 504, start_pos_y + 204, 92, 92],  2* PI - PI * 0.25, PI * 2, 4)
    pygame.draw.arc(screen, BLUE, [start_pos + 504, start_pos_y + 204, 92, 92], 0, PI * 0.25, 4)

    if start_pos + 550 + 65 >= 700 or start_pos + 50 <= 0:
        x_speed = 0

    if start_pos_y + 300 >= 500 or start_pos_y + 200 <= 0:
        y_speed = 0


    player_image.set_colorkey(BLACK)


    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy image to screen:
    screen.blit(player_image, [x, y])

    pygame.display.flip()






    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()