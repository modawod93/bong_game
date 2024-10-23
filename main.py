from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from left_paddle_ai import move_left_paddle_ai

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Ask the user to choose the game mode
game_mode = screen.textinput("Choose Game Mode", "Type '1' for single-player (vs computer) or '2' for two-player: ")

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Move the left paddle if the game mode is single-player (vs computer)
    if game_mode == '1':
        move_left_paddle_ai(ball, l_paddle, scoreboard.r_score)

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Check for winner
    game_is_on = scoreboard.check_for_winner(screen, ball)

screen.exitonclick()
