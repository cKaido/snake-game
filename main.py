from turtle import Turtle, Screen, color

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")

x_coord = [0, -20, -40]
new_snake = []

for location in range(0, 3):
    snake = Turtle(shape="square")
    snake.color('white')
    snake.goto(x=x_coord[location], y=0)


screen.exitonclick()
