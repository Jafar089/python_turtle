import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
t.speed(1)
t.color('white')


def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)


t.fillcolor('red')
t.begin_fill()
t.left(140)
t.forward(113)
curve()
t.left(120)
curve()
t.forward(112)
t.end_fill()


t.up()
t.goto(-45,90)
t.down()
t.fillcolor('dark blue')
t.begin_fill()
t.write("I Like You",font=("Verdana",16, "italic"))
t.end_fill()


t.up()
t.goto(-120,-50)
t.down()
t.begin_fill()
t.fillcolor('yellow')
t.write("Will You Be My Friend..!",font=("Verdana",16, "italic"))
t.end_fill()
t.hideturtle()

while True:
  wn.update()