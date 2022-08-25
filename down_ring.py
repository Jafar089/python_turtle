import turtle

t = turtle.Turtle()
wn = turtle.Screen()

t.color('brown')

t.up()
t.goto(0,250)
t.dot('red')
for x in range(-450,460,100):
    t.up()
    t.goto(0,250)
    t.down()
    t.goto(x,-250)
    t.dot('blue')

t.hideturtle()
wn.mainloop()