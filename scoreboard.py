from turtle import Turtle
FONT = ("Courier", 24, "normal")
RIGHT = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 1
        self.right = RIGHT
        self.hideturtle()
        self.goto(-120, 260)
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score} Right : {self.right}", align="center", font=FONT)

    def score_up(self):
        self.score += 1
        self.update_score()

    def game_on(self):
        self.right -= 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def control(self):
        if self.right < 1:
            self.game_over()
            return False
        else:
            return True

