import random
import turtle
from turtle import Turtle, Screen

color = ['red', 'yellow','blue', 'green', 'orange']
all_turtle = []
is_race_on = False

screen = Screen()
screen.setup(height=400, width=500)


user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Choose a color:").lower()
for turtle_index in range(1, 6):
    new_turtle = Turtle(shape="turtle")
    x_coordinate = -230
    y_coordinate = -100 + (turtle_index * 30)
    new_turtle.penup()
    new_turtle.color(color[turtle_index - 1])
    new_turtle.goto(x=x_coordinate, y=y_coordinate)
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:

        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You have Won! The {winning_color} is the winner.")
            else:
                print(f"You have lost! The {winning_color} is the winner.")

        random_distance= random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()