import turtle

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('black')
t.color('white')
t.speed(0)
t.left(90)

for i in range(36):
    t.left(10)
    t.fd(250)
    t.bk(250)
    t.left(360)

t.up()
t.goto(-30,0)
t.down()
t.right(180)
rad = 30
x=-30
for i in range(10):
    t.circle(rad)
    t.up()
    x=x-25
    t.goto(x,0)
    t.down()
    rad=rad+25



wn.mainloop()