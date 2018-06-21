from sense_hat import SenseHat
from apple import Apple


class Snake:
    def __init__(self, x, y, length, field, rgb):
        self.sense = SenseHat()
        self.apple = Apple(field, (133, 0, 0))
        self.x = x + length
        self.y = y + length
        self.length = length
        self.field = field
        self.rgb = rgb

    def boot(self):
        self.sense.set_pixel(self.x, self.y, self.rgb)

    def up(self):
        self.remove()
        if self.y != 0:
            self.y -= 1
        else:
            self.y = self.field
        self.update()

    def down(self):
        self.remove()
        if self.y != self.field:
            self.y += 1
        else:
            self.y = 0
        self.update()

    def left(self):
        self.remove()
        if self.x != 0:
            self.x -= 1
        else:
            self.x = self.field
        self.update()

    def right(self):
        self.remove()
        if self.x != self.field:
            self.x += 1
        else:
            self.x = 0
        self.update()

    def remove(self):
        self.sense.set_pixel(self.x, self.y, 0, 0, 0)

    def update(self):
        if self.sense.get_pixel(self.x, self.y) == (200, 0, 0):  # red
            self.length += 1
            self.apple.remove()
            self.apple.create()
            self.sense.set_pixel(self.x, self.y, self.rgb)
        elif self.sense.get_pixel(self.x, self.y) == self.rgb:  # lose
            self.sense.show_message("You lose!", scroll_speed=0.05)
        else:
            self.sense.set_pixel(self.x, self.y, self.rgb)
            return