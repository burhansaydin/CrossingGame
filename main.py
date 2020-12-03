import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_left()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            if scoreboard.control():
                scoreboard.game_on()
                player.go_to_start()
            else:
                game_is_on = False

    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score_up()

screen.exitonclick()
