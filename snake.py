class Snake:
    def __init__(self, sense, rgb, apple, nap):
        self.sense = sense
        self.rgb = rgb
        self.xy = [(0, 0)]
        self.apple = apple
        self.nap = nap

    def boot(self):
        self.sense.set_pixel(self.xy[0][0], self.xy[0][1], self.rgb)
        self.apple.create()

    def up(self):
        x = self.xy[0][0]
        y = self.xy[0][1]
        if y != 0:
            self.move(x, y - 1)
        else:
            self.move(x, 7)

    def down(self):
        x = self.xy[0][0]
        y = self.xy[0][1]
        if y != 7:
            self.move(x, y + 1)
        else:
            self.move(x, 0)

    def left(self):
        x = self.xy[0][0]
        y = self.xy[0][1]
        if x != 0:
            self.move(x - 1, y)
        else:
            self.move(7, y)

    def right(self):
        x = self.xy[0][0]
        y = self.xy[0][1]
        if x != 7:
            self.move(x + 1, y)
        else:
            self.move(0, y)

    def move(self, x, y):
        if (x, y) == (self.apple.x, self.apple.y):
            self.apple.create()
            self.nap *= 0.95
        elif (x, y) in self.xy:
            self.nap = -1
        else:
            self.remove_last()
        self.add_head(x, y)

    def remove_last(self):
        self.sense.set_pixel(self.xy[-1][0], self.xy[-1][1], 0, 0, 0)
        self.xy.remove(self.xy[-1])

    def add_head(self, x, y):
        self.xy.insert(0, (x, y))
        self.sense.set_pixel(x, y, self.rgb)
