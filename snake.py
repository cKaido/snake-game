from turtle import Turtle
X_COORD = [0, -20, -40]


class Snake:

    def __init__(self):
        self.new_snake = []
        self.create_snake()

    def create_snake(self):
        for coord in range(0, 3):
            snake = Turtle(shape="square")
            snake.color('white')
            snake.penup()
            snake.goto(x=X_COORD[coord], y=0)
            self.new_snake.append(snake)

    def move(self):
        for snake_num in range(len(self.new_snake) - 1, 0, -1):
            new_x = self.new_snake[snake_num - 1].xcor()
            new_y = self.new_snake[snake_num - 1].ycor()
            self.new_snake[snake_num].goto(new_x, new_y)
