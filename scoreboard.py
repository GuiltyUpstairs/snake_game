from turtle import Turtle
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over (You suck)", align="center", font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("Arial", 20, "normal"))