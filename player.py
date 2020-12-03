from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()
        self.new_y = self.ycor()
        self.new_x = self.xcor()

    def move(self):
        self.new_y += 10
        self.goto(0, self.new_y)
        if self.new_y > FINISH_LINE_Y:
            self.new_y = -280

    def move_down(self):
        self.new_y -= 10
        self.goto(0, self.new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
        self.new_y = 280

    def is_at_finishline(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
