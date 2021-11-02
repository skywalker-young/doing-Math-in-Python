# import turtle
# t=turtle.Pen()
# t.pencolor('black')
# t.fillcolor("red")
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.end_fill()
#
# t.left(90)
#
# t.fillcolor('black')
# t.begin_fill()
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.left(180)
# t.end_fill()
#
# t.fillcolor('black')
# t.begin_fill()
# for a in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.end_fill()
#
# t.fillcolor('red')
# t.begin_fill()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.end_fill()
# t.end_fill()
#
# turtle.done()


# import turtle
# t=turtle.Pen()
# t.pencolor('black')
# t.fillcolor("red")
# for i in range(4):
#     t.forward(100)
#     t.left(90)
# t.end_fill()
#
# t.left(90)
#
# t.fillcolor('black')
# t.begin_fill()
# for i in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.left(180)
# t.end_fill()
#
# t.fillcolor('black')
# t.begin_fill()
# for a in range(4):
#     t.forward(100)
#     t.left(90)
#
# t.end_fill()
#
# t.fillcolor('red')
# t.begin_fill()
# for i in range(4):
#     t.forward(100)
#     t.right(90)
# t.end_fill()
# t.end_fill()
#
# turtle.done()
#
# import turtle
#
# t=turtle.Pen()
#
# t.fillcolor('lime')
# t.begin_fill()
#
# t.circle(50)
#
# t.end_fill()
#
# t.fillcolor('yellow')
# t.begin_fill()
# t.circle(-50)
# t.end_fill()
#
# t.left(180)
#
# t.penup()
# t.goto(x=50,y=-50)
# t.fillcolor('red')
# t.begin_fill()
# t.circle(-50)
# t.end_fill()
#
# t.penup()
# t.goto(x=-50,y=-50)
# t.pendown()
#
# t.fillcolor('black')
# t.begin_fill()
# t.circle(-50,-360)
# t.end_fill()
# turtle.done()

import turtle

turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(10)
#主星
turtle.begin_fill()
turtle.up()
turtle.goto(-600,220)
turtle.down()
for i in range (5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()

#第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,295)
turtle.setheading(305)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()


#第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,212)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第3颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,145)
turtle.setheading(5)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第4颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,90)
turtle.setheading(300)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()

turtle.done()
