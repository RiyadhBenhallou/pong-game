from turtle import Turtle, Screen
from ball import Ball
import time
from paddle import Paddle
from random import randint, random

from scoreboard import Scoreboard

screen = Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.screensize(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()


screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

paddles = [(l_paddle, -320), (r_paddle, 320)]

game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  ball.move()
  screen.update()
  if ball.ycor() > 150 or ball.ycor() < -150:
    ball.bounce_y()
  for paddle in paddles:
    if ball.distance(paddle[0]) < 50 and ball.xcor() > paddle[1]:
      ball.bounce_x()
        

  if ball.xcor() > 380:
    scoreboard.l_score += 1
    scoreboard.update()
    ball.reset_position()
  elif ball.xcor() < -380:
    scoreboard.r_score += 1
    scoreboard.update()
    ball.reset_position()
    

screen.exitonclick()