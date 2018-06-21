class Snake:
    def __init__(self, sense, field, rgb, x, y, length, apple):
        self.sense = sense
        self.field = field
        self.rgb = rgb
        self.x = x
        self.y = y
        self.length = length
        self.apple = apple

    def boot(self):
        self.sense.set_pixel(self.x, self.y, self.rgb)
        self.apple.create()

    def up(self):
        y = self.y
        if y != 0:
            y -= 1
        else:
            y = self.field - 1
        self.move(self.x, y)

    def down(self):
        y = self.y
        if y != self.field - 1:
            y += 1
        else:
            y = 0
        self.move(self.x, y)

    def left(self):
        x = self.x
        if x != 0:
            x -= 1
        else:
            x = self.field - 1
        self.move(x, self.y)

    def right(self):
        x = self.x
        if x != self.field - 1:
            x += 1
        else:
            x = 0
        self.move(x, self.y)

    def remove(self):
        self.sense.set_pixel(self.x, self.y, 0, 0, 0)

    def update(self):
        self.sense.set_pixel(self.x, self.y, self.rgb)

    def move(self, x, y):
        if self.sense.get_pixel(x, y) == self.apple.rgb:
            self.length += 1
            self.apple.create()
            self.sense.set_pixel(self.x, self.y, self.rgb)
        elif self.sense.get_pixel(self.x, self.y) == self.rgb:
            self.sense.show_message("You lose!", scroll_speed=0.05)
        else:
            self.remove()
            self.sense.set_pixel(self.x, self.y, self.rgb)
        self.x = x
        self.y = y
