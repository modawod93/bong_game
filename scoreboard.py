from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def check_for_winner(self, screen, ball):
        if self.l_score == 10 or self.r_score == 10:
            winner = "Left" if self.l_score == 10 else "Right"
            play_again = screen.textinput("Game Over", f"{winner} paddle wins! Do you want to restart? (yes/no): ")
            if play_again.lower() == "yes":
                self.l_score = 0
                self.r_score = 0
                self.update_scoreboard()
                ball.reset_position()
            else:
                return False
        return True
