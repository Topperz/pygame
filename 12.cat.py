__author__ = 'Topper121'

class Cat:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = 0

    def meow(self):
        print("meow!")


newcat = Cat()

newcat.meow()

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 100
        print("A dog has been born!")

    def decreaseHealth(self, amount):
        if self.health < 0:
            print(self.name + " has died")
        else:
            self.health -= amount

dog = Monster("logos")