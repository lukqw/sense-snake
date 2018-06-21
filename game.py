from sense_hat import SenseHat
from sensimate import SensiMate
from apple import Apple
from snake import Snake

from time import sleep


class Game:

    def __init__(self, field):
        self.sense = SenseHat()
        self.sense.clear()
        self.sense.rotation = 180
        self.sense.low_light = True
        self.field = field
        self.sensimate = SensiMate(self.sense, self.field)
        self.apple = Apple(self.sense, self.field, (200, 0, 0))
        self.snake = Snake(self.sense, self.field, (0, 133, 0), 0, 0, self.apple)
        self.start()

    def start(self):
        self.animate_start()
        self.game_start()

    def animate_start(self):
        self.sensimate.spiral(0.01, (148, 0, 211))
        self.sensimate.spiral(0.01, (75, 0, 130))
        self.sensimate.spiral(0.01, (0, 0, 255))
        self.sensimate.spiral(0.01, (0, 255, 0))
        self.sensimate.spiral(0.01, (255, 255, 0))
        self.sensimate.spiral(0.01, (255, 127, 0))
        self.sensimate.spiral(0.01, (255, 0, 0))
        self.sense.show_message("Snake", scroll_speed=0.05)
        self.sensimate.countdown(3)
        self.sense.clear()

    def game_start(self):
        self.snake.boot()
        direction = "right"
        while True:
            sleep(1)
            if direction == "up":
                self.snake.up()
            elif direction == "down":
                self.snake.down()
            elif direction == "left":
                self.snake.left()
            elif direction == "right":
                self.snake.right()
            events = self.sense.stick.get_events()
            if len(events) > 0:
                direction = events[len(events) - 1].direction


game = Game(8)
