from sense_hat import SenseHat
from sensimate import SensiMate
from apple import Apple
from snake import Snake

from time import sleep


class Game:

    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.sense.low_light = True
        self.sensimate = SensiMate(self.sense)
        self.apple = Apple(self.sense, (200, 0, 0))
        self.snake = Snake(self.sense, (0, 133, 0), self.apple, 1)
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
            if self.snake.nap != -1:
                sleep(self.snake.nap)
                events = self.sense.stick.get_events()
                if len(events) > 0:
                    newdirection = events[len(events) - 1].direction
                    if not ((direction == "up" and newdirection == "down")
                            or (direction == "down" and newdirection == "up")
                            or (direction == "left" and newdirection == "right")
                            or (direction == "right" and newdirection == "left")):
                        direction = newdirection
                if direction == "up":
                    self.snake.up()
                elif direction == "down":
                    self.snake.down()
                elif direction == "left":
                    self.snake.left()
                elif direction == "right":
                    self.snake.right()
            else:
                self.sense.show_message("You lose!", scroll_speed=0.05)
                self.sense.show_message("Score: %d" % len(self.snake.xy), scroll_speed=0.05)


game = Game()
