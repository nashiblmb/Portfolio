import turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.current_score()

    def current_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.current_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

