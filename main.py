from turtle import Screen
import time
import player as p
import car_manager as cm
import scoreboard as sb

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = p.Player()
car_manager = cm.CarManager()
scoreboard = sb.Scoreboard()

screen.listen()
screen.onkey(player.up ,"Up")

game_continue = True
while game_continue:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_continue = False
            scoreboard.game_over()
    if player.at_finish():
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
