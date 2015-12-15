__author__ = 'Topper121'

import random
import blocks

GREEN = (  0, 255,   0)

class Goodblock(blocks.Block):
    def __init__(self):

        # Call the parent class (Sprite) constructor
        super().__init__(GREEN, 20, 15)

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += random.randrange(-3,4)
        self.rect.y += random.randrange(-3,4)








