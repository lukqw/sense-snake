import random


class Apple:
    def __init__(self, field, rgb, sense):
        self.sense = sense
        self.field = field
        self.rgb = rgb
        self.x = 0
        self.y = 0
        self.create()

    def create(self):
        self.x = random.randint(0, self.field - 1)
        self.y = random.randint(0, self.field - 1)
        if self.sense.get_pixel(self.x, self.y) != (0, 0, 0):
            self.create()
        self.sense.set_pixel(self.x, self.y, self.rgb)

    def remove(self):
        self.sense.set_pixel(self.x, self.y, 0, 0, 0)
