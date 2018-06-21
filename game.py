from sense_hat import SenseHat
from time import sleep
from snake import Snake
from sensimate import SensiMate


class Game:

    def __init__(self):
        self.sense = SenseHat()
        self.sense.rotation = 180
        self.sense.low_light = True
	self.sense.clear()
        self.field = 8
        self.snake = Snake(0, 0, 1, self.field, (0, 133, 0), self.sense)
        self.sensimate = SensiMate(self.field, self.sense)
        self.start()

    def start(self):
        self.animate_start()
        self.game_start()

    def animate_start(self):
        self.sense.clear()
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
	    if(len(events) > 0):
                direction = events[len(events)-1].direction

game = Game()
game.start()
