from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 13, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=280)
        self.score = 0
        self.high_score = self.read_file()
        self.update_scoreboard()

    def read_file(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        return self.high_score

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f'Score: {self.score} High Score: {self.high_score} ', True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
