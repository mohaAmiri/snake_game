from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("white")
        self.speed('fastest')
        self.refresh()  # to have a random position at the beginning

    def refresh(self):
        """ show the food in random position """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)
