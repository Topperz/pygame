__author__ = 'Topper121'

import random
import blocks

RED = (  255, 0,   0)

class Badblock(blocks.Block):
    def __init__(self):

        # Call the parent class (Sprite) constructor
        super().__init__(RED, 20, 15)

    def update(self):
        """ Find a new position for the player"""
        self.rect.x += random.randrange(-3,4)
        self.rect.y += random.randrange(-1,4)