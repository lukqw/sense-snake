import random


class Apple:
    def __init__(self, sense, field, rgb):
        self.sense = sense
        self.field = field
        self.rgb = rgb

    def create(self):
        x = random.randint(0, self.field - 1)
        y = random.randint(0, self.field - 1)
        if self.sense.get_pixel(x, y) == [0, 0, 0]:
            self.sense.set_pixel(x, y, self.rgb)
        else:
            self.create()
