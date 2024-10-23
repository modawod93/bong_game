import random

def move_left_paddle_ai(ball, l_paddle, r_score):
    """
    Moves the left paddle AI with increasing accuracy as the right player scores more points.
    
    :param ball: The ball object.
    :param l_paddle: The left paddle object.
    :param r_score: The score of the right player (user).
    """
    # Base responsiveness; starts lower and increases with r_score
    base_probability = 0.5 + (r_score * 0.05)  # Increase responsiveness by 2% per score
    base_probability = min(base_probability, 1)  # Cap probability at 1 (100% accuracy)

    if random.random() < base_probability:  # Chance for the paddle to move towards the ball
        if ball.ycor() > l_paddle.ycor():
            l_paddle.go_up()
        elif ball.ycor() < l_paddle.ycor():
            l_paddle.go_down()
