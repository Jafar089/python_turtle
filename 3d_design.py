import turtle

t =turtle.Turtle()
t.color('white')
wn = turtle.Screen()
wn.bgcolor('black')

t.begin_fill()
t.fillcolor('yellow')
t.goto(-100,0)
t.rt(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(60)
t.fd(100)
t.end_fill()


t.begin_fill()
t.fillcolor('green')
t.rt(60)
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(120)
t.fd(100)
t.rt(60)
t.fd(100)
t.end_fill()



t.begin_fill()
t.fillcolor('blue')
t.fd(100)
t.rt(60)
t.fd(100)
t.rt(120)
t.fd(100)
t.rt(60)
t.fd(100)
t.end_fill()
t.hideturtle()

wn.mainloop()





# circle ring

# import turtle

# t = turtle.Turtle()

# wn = turtle.Screen()
# t.pensize(3)
# l1 = ['yellow','red','blue','purple','green','black','orange','pink','brown']
# rad=20
# t.up()
# t.goto(0,-100)
# t.down()
# for i in range(9):
#     t.pencolor(l1[i])
#     t.circle(rad)
#     rad+=20

# t.hideturtle()
# wn.mainloop()


