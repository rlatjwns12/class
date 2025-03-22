import turtle as t
import random as r

me = t.Turtle()
me.shape('square')
me.color('blue')
me.penup()

apple = t.Turtle()
apple.shape('circle')
apple.color('red')
apple.penup()

def move_up():
    me.setheading(90)

def move_down():
    me.setheading(270)

def move_left():
    me.setheading(180)

def move_right():
    me.setheading(0)

def apple_move():
    apple.ht()
    apple.setx(r.randint(-200,200))
    apple.sety(r.randint(-200,200))
    apple.st()

def display_score():
    score_turtle.clear()
    score_turtle.write(score,font=('Comic Sans MS',30,'bold'))

score = 0

score_turtle = t.Turtle()
score_turtle.ht()
score_turtle.penup()
x = t.window_width()/3
y = t.window_height()/3
score_turtle.setpos(x,y)

def outside_window():
    (x,y) = me.pos()
    outside = x < -t.window_width() / 2 or \
    x > t.window_width() / 2 or \
    y < -t.window_height() / 2 or \
    y > t.window_height() / 2
    return outside

def game_over():
    score_turtle.clear()
    score_turtle.write('GAME OVER!', align="right", font = ('Comic Sans MS', 30, 'normal'))

obstacles = []

def create_obstacle():
    obstacle = t.Turtle()
    obstacle.ht()
    obstacle.shape('triangle')
    obstacle.color('black')
    obstacle.penup()
    obstacle.setx(r.randint(-200,200))
    obstacle.sety(r.randint(-200,200))
    obstacle.st()
    obstacles.append(obstacle)


def start():
    global score
    apple_move()
    display_score()
    isFinish = False
    while True:
        if outside_window():
           game_over()
           break
        me.forward(score // 10 + 1)
        if me.distance(apple) <= 20:
            apple_move()
            score = score + 10
            display_score()
            create_obstacle()
        for obstacle in obstacles:
            print("obstacle")
            if me.distance(obstacle) < 20:
                print("distance obstalce")
                game_over()
                isFinish = True
                break
        if isFinish:
            break

t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(move_right,'Right')
t.onkey(start,'space')
t.listen()

t.mainloop()