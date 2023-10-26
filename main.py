from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(600,600)

screen.bgcolor("black")
screen.title("my snake game")
#position=[(0,0),(-20,0),(-40,0)]
# segments=[]
# x=0
# y=0
screen.tracer(0)


# for _ in range(3):
#     new_turtle=Turtle(shape="square")
#
#
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(x,y)
#     segments.append(new_turtle)
#     x-=20

score=ScoreBoard()
snake=Snake()
food=Food()

8


screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    #detect collosion with food
    if (snake.head.distance(food)<12):
        food.refresh()
        score.new_score()
        snake.extend()

    #detect collosion with  wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290) or (snake.head.ycor() > 290 or snake.head.ycor() < -290):
        # snake.head.done()
        score.reset()
        snake.reset_snake()
        game_is_on = False
        score.game_over()
    #detect collosion with tail
    #if head collides with any segments wih tail
    #trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
                  score.reset()
                  game_is_on=False
                  score.game_over()


screen.exitonclick()