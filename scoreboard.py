from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode="r") as data:
            self.high_score = int(data.read())
        self.clear()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ update after increasing score or game over """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """ reset score after game over """
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def welcome(self):
        """ print instruction at the beginning """
        self.welcome_message = Turtle()
        self.welcome_message.penup()
        self.welcome_message.color("white")
        self.welcome_message.goto(0, 0)
        self.welcome_message.hideturtle()
        self.welcome_message.write("Press Enter to start!", align="center", font=("Courier", 24, "normal"))
        self.welcome_message.goto(0, -50)
        self.welcome_message.write("Click on screen to quit!", align="center", font=("Courier", 18, "normal"))
