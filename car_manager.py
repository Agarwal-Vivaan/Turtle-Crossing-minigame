import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        chance = random.randint(1, 5)
        if chance == 5:
            random_y = random.randint(-250, 250)
            for car in self.all_cars:
                if car.xcor() > 250 and abs(car.ycor()) < 20:
                    return
            new_car = turtle.Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars[:]:
            if cars.xcor() < -320:
                cars.hideturtle()
                self.all_cars.remove(cars)
            cars.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
