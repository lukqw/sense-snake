from time import sleep


class SensiMate:
    def __init__(self, field, sense):
        self.sense = sense
        self.field = field

    def spiral(self, nap, rgb):
        dx, dy = 1, 0
        x, y = 0, 0
        array = [[None] * self.field for j in range(self.field)]
        for i in range(self.field ** 2):
            sleep(nap)
            self.sense.set_pixel(x, y, rgb)
            array[x][y] = i
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.field and 0 <= ny < self.field and array[nx][ny] == None:
                x, y = nx, ny
            else:
                dx, dy = -dy, dx
                x, y = x + dx, y + dy

    def countdown(self, n):
        for i in range(n, 0, -1):
            self.sense.show_letter(str(i))
            sleep(1)
