from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        super().__init__()
        self.num = len(self.all_cars)

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-280, 280))
            self.all_cars.append(new_car)

    def move_left(self):
        for i in self.all_cars:
            i.forward(STARTING_MOVE_DISTANCE)
