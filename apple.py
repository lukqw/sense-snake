import random


class Apple:
    def __init__(self, sense, rgb):
        self.sense = sense
        self.rgb = rgb
        self.x = 0
        self.y = 0

    def create(self):
        self.x = random.randint(0, 7)
        self.y = random.randint(0, 7)
        if self.sense.get_pixel(self.x, self.y) == [0, 0, 0]:
            self.sense.set_pixel(self.x, self.y, self.rgb)
        else:
            self.create()
