
from turtle import Turtle


class Paddle(Turtle):
  def __init__(self, pos):
    super().__init__()
    self.color('white')
    self.shape('square')
    self.shapesize(5, 1)
    self.penup()
    self.goto(pos)

  def up(self):
    y = self.ycor() + 20
    self.goto(self.xcor(), y)

  def down(self):
    y = self.ycor() - 20
    self.goto(self.xcor(), y)