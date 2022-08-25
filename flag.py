import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.pensize(3)
t.up()
t.goto(0,-220)
t.down()
t.goto(0,250)
for i in range(3):
    t.forward(220)
    t.right(90)

t.right(90)

t.forward(80)
t.right(270)
t.forward(220)

t.begin_fill()
t.fillcolor('green')
for i in range(2):
  t.right(90)
  t.forward(140)
  t.right(90)
  t.forward(220)
t.end_fill()


# making moon here
t.color('white')
t.up()
t.goto(0,0)
t.goto(200,140)
t.down()

t.begin_fill()
t.fillcolor('white')
t.circle(50)
t.end_fill()

t.up()
t.left(90)
t.forward(85)
t.left(90)
t.begin_fill()
t.fillcolor('green')
t.circle(50)
t.end_fill()


# making star here

t.up()
t.goto(0,0)
t.goto(160,165)
t.down()

t.begin_fill()
t.fillcolor('white')
for i in range(5):
  t.forward(50)
  t.right(144)
t.end_fill()
t.hideturtle()
while True:
  wn.update()