from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()        
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 50
        if new_y <= 250:  # Ensure the paddle does not go beyond the top limit
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 50
        if new_y >= -250:  # Ensure the paddle does not go beyond the bottom limit
            self.goto(self.xcor(), new_y)
