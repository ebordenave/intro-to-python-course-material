class Ogre:

    def __init__(self, size, color, strength, health, name):
        self.health = health
        self.size = size
        self.color = color
        self.strength = strength
        self.name = name

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


shrek_the_ogre = Ogre('Large', 'Green', '5', '100', 'Shrek')

print(shrek_the_ogre.name)
