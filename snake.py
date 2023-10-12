import turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create()


    def create(self):
        for i in range(0, 3):
            new_turtle = turtle.Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(0 - (i * 20), 0)
            self.segments.append(new_turtle)

    def collision(self):
        for i in range(3, len(self.segments)):
            if self.segments[0].distance(self.segments[i]) < 10:
                return True

    def extend(self, x, y):
        new_turtle = turtle.Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(x, y)
        self.segments.append(new_turtle)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create()
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(-90)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)