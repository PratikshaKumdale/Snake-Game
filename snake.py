# class Snake:
#     def __init__(self,segments):
#         self.a=segments
#
#
#     def move(self, a):
#         for seg_num in range(2, 0, -1):
#             x = a[seg_num - 1].xcor()
#             y = a[seg_num - 1].ycor()
#             a[seg_num].goto(x, y)
#         a[0].forward(20)
from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        #
        self.x=0
        self.y=0
        self.create()
        self.head=self.segments[0]

    def create(self):
        for _ in range(3):
            new_turtle = Turtle(shape="circle")

            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(self.x, self.y)
            self.segments.append(new_turtle)
            self.x -= 20
    def add_segment(self):
        new_turtle = Turtle(shape="circle")
        new_turtle.goto(self.segments[-1].pos())
        new_turtle.color("white")
        new_turtle.penup()
        self.segments.append(new_turtle)

    def extend(self):
        # o=self.segments[-1]

        self.add_segment()

    def reset_snake(self):
        for seg  in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create()
        self.head=self.segments[0]
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.segments[0].forward(20)
        # if (self.head.xcor()>300 or self.head.xcor()<-300) or(self.head.ycor()>300 or self.head.ycor()<-300):
        #     self.head.done()


    def up(self):
        if (self.head.heading()!= DOWN):
            self.head.seth(UP)
    def down(self):
         if( self.head.heading()!=UP):
             self.head.seth(DOWN)
    def right(self):
         if (self.head.heading()!=LEFT):
             self.head.seth(RIGHT)
    def left(self):
        if (self.head.heading()!=RIGHT):
             self.head.seth(LEFT)


