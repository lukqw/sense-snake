class Snake:
    def __init__(self, sense, field, rgb, x, y, apple):
        self.sense = sense
        self.field = field
        self.rgb = rgb
        self.xy = [(x, y)]
        self.apple = apple

    def boot(self):
        self.sense.set_pixel(self.xy[0], self.rgb)
        self.apple.create()

    def up(self):
        y = self.xy[0][1]
        if y != 0:
            y -= 1
        else:
            y = self.field - 1
        self.move(self.x, y)

    def down(self):
        y = self.xy[0][1]
        if y != self.field - 1:
            y += 1
        else:
            y = 0
        self.move(self.x, y)

    def left(self):
        x = self.xy[0][0]
        if x != 0:
            x -= 1
        else:
            x = self.field - 1
        self.move(x, self.y)

    def right(self):
        x = self.xy[0][0]
        if x != self.field - 1:
            x += 1
        else:
            x = 0
        self.move(x, self.y)

    def move(self, x, y):
        if (x, y) == (self.apple.x, self.apple.y):
            self.apple.create()
        elif (x, y) in self.xy:
            self.sense.show_message("You lose!", scroll_speed=0.05)
        else:
            self.xy.remove((x, y))
        self.sense.set_pixel(x, y, self.rgb)
        self.xy.append((x, y))
