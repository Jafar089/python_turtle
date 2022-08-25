import turtle
j = turtle.Turtle()
j.color('white')
wn = turtle.Screen()
wn.bgcolor('white')
wn.title('Turtle')
turtle.colormode(255)
wn.bgcolor(50,60,30)
wn.bgpic('jafar 1.gif')


# motions of turtle

# j.setheading(90)
# j.setheading(180)
# j.setheading(270)
# j.setheading(360)

# j.fd(100)
# j.backward(200)

# j.forward(100)
# j.left(45)
# j.forward(100)

# j.forward(100)
# j.right(75)
# j.forward(100)


# # draw square through turtle
# j.forward(100)
# j.left(90)
# j.forward(100)
# j.left(90)
# j.forward(100)
# j.left(90)
# j.forward(100)

# # or square through this method

# j.speed(3)

# j.begin_fill()
# j.fillcolor('red')
# for i in range(4):
#     j.forward(100)
#     j.left(90)

# j.hideturtle()
# j.end_fill()


# # draw circle through turtle

# j.circle(-50)
# j.circle(100,180)
# j.circle(100,steps=3)

# j.up()
# j.goto(0,-100)
# j.down()
# j.circle(100)

# j.up()
# j.goto(50,50)
# j.down()
# j.circle(100)



# # draw 5 circles shape
# def draw_circles(x,y,color,rad):
#     j.up()
#     j.goto(x,y)
#     j.down()
#     j.begin_fill()
#     j.fillcolor(color)
#     j.circle(rad)
#     j.end_fill()
#     j.up()
#     j.home()


# j.speed(10)
# j.pensize(4)
# draw_circles(0, -50, "green", 50)
# draw_circles(0, 300, "green", 25)
# draw_circles(200, 200, "orange", 50)
# draw_circles(0, -300, "orange", 25)
# draw_circles(-200, 200, "blue", 50)
# draw_circles(300, 0, "blue", 25)
# draw_circles(-200, -200, "red", -50)
# draw_circles(-300, 0, "red", 25)
# draw_circles(200, -200, "yellow", -50)


# # draw other circle shapes

# l1 = ['yellow','red','blue','green']
# j.up()
# j.goto(200,0)

# for i in range(4):
#     j.down()
#     j.begin_fill()
#     j.fillcolor(l1[i])
#     j.circle(50)
#     j.end_fill()
#     j.up()
#     j.bk(100)

# for i in range(4):
#     j.down()
#     j.color(l1[i])
#     j.pensize(20)
#     j.circle(100)
#     j.up()
#     j.bk(100)



# # draw another shape
# l1 = ['purple','red','orange','darkblue','green']
# j.speed(0)
# for i in range(200):
#     j.color(l1[i%5])
#     j.pensize(i/9+1)
#     j.forward(i)
#     j.left(59)



# draw pakistani flag thorugh turtle
wn.bgcolor('green')
j.up()
j.goto(0,-200)
j.color('white')
j.begin_fill()
j.circle(200)
j.end_fill()

j.up()
j.goto(50,-200)
j.color('green')
j.begin_fill()
j.circle(200)
j.end_fill()

while True:
  wn.update()