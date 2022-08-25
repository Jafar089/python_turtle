from turtle import *
pen = Turtle()

colors = ["red", "green", "blue"]

while 1:
    i = 0
    for x in range(len(colors)):
        pen.dot(100, colors[i])
        i += 1

