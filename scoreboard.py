from  turtle import Turtle
ALIGN="center"
FONT=("bold",20)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.count=0
        with open("data.txt") as data:
            self.highscore=int(data.read())

        self.pencolor("white")
        # self.write(f"score:{self.count}", align="center", font=("bold", 20))
        self.new_score()


    def new_score(self):
        self.clear()
        self.write(f"score:{self.count}  High score={self.highscore}",align=ALIGN,font=FONT)
        self.count += 1

    def reset(self):
        if self.count>self.highscore:
            self.highscore=self.count-1
            with open("data.txt",mode="w") as data :
                data.write(f"{self.highscore}")
        self.count=0
        self.new_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER  SCORE:{self.count}",align=ALIGN,font=FONT)