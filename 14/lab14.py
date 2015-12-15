__author__ = 'Topper121'

"""
Use sprites to collect blocks.

"""
import pygame
import random
import blocks
import goodblocks
import badblocks
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)


class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # -- Methods
    def __init__(self, color, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 11])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # -- Attributes
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Find a new position for the player"""
        if self.rect.x <= 0 or self.rect.x + 15 >= 700:
            self.rect.x = 350
        if self.rect.y <= 0 or self.rect.y + 10 >= 400:
            self.rect.y = 200
        self.rect.x += self.change_x
        self.rect.y += self.change_y

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)

red_sound = pygame.mixer.Sound("laser5.ogg")

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
good_block_list = pygame.sprite.Group()
bad_block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = goodblocks.Goodblock()

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    good_block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
    # This represents a block
    block = badblocks.Badblock()

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    bad_block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Player(BLUE, 20, 15)
#all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    # Moves the player and update the blocks
    all_sprites_list.update()
    player.update()
    # Clear the screen
    screen.fill(WHITE)

    x = player.rect.x
    y = player.rect.y

    # Copy image to screen:
    screen.blit(player_image, [x, y])

    # See if the player block has collided with anything.
    good_blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
    bad_blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
    # Check the list of collisions.
    for block in good_blocks_hit_list:
        score += 1
        print(score)

    for block in bad_blocks_hit_list:
        score -= 1
        print(score)
        red_sound.play()

    # Draw all the spites
    all_sprites_list.draw(screen)

    # SCore
    score1 = str(score)
    font = pygame.font.SysFont("serif", 25)
    text = font.render("Score is: " + score1, True, BLACK)
    center_x = (50)
    center_y = (350)
    screen.blit(text, [center_x, center_y])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(20)

pygame.quit()