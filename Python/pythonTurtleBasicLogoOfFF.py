import turtle
f=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("white")
def drawF(x:int,y:int):
    f.color("black")
    f.up()
    f.goto(x,y)
    f.down()
    f.begin_fill()
    f.setheading(360)
    f.forward(150)
    f.right(90)
    f.forward(50)
    f.right(90)
    f.forward(100)
    f.left(90)
    f.forward(50)
    f.left(90)
    f.forward(90)
    f.right(90)
    f.forward(50)
    f.right(90)
    f.forward(90)
    f.left(90)
    f.forward(150)
    f.right(90)
    f.forward(50)
    f.goto(x,y)
    f.end_fill()
def drawR(x:int,y:int):
    f.color("black")
    f.up()
    f.goto(x,y)
    f.down()
    f.begin_fill()
    f.setheading(360)
    f.fd(75)
    f.circle(-90,155)
    f.setheading(300)
    f.fd(125)
    f.rt(90)
    f.fd(50)
    f.rt(90)
    f.goto(x+50,y-150)
    f.setheading(270)
    f.fd(150)
    f.rt(90)
    f.fd(50)
    f.goto(x,y)
    f.end_fill()
    f.up()
    f.goto(x+50,y-50)
    f.down()
    f.begin_fill()
    f.fillcolor("white")
    f.seth(360)
    f.fd(25)
    f.circle(-40,180)
    f.fd(25)
    f.seth(90)
    f.fd(80)
    f.end_fill()
def drawE(x:int,y:int):
    f.color("black")
    f.up()
    f.goto(x,y)
    f.down()
    f.begin_fill()
    f.seth(360)
    f.fd(150)
    f.rt(90)
    f.fd(60)#
    f.rt(90)
    f.fd(100)
    f.lt(90)
    f.fd(60)#
    f.lt(90)
    f.fd(70)
    f.rt(90)
    f.fd(60)#
    f.rt(90)
    f.fd(70)
    f.lt(90)
    f.fd(60)#
    f.lt(90)
    f.fd(100)
    f.rt(90)
    f.fd(60)#
    f.rt(90)
    f.fd(150)
    f.rt(90)
    f.goto(x,y)
    f.end_fill()
def drawI(x:int,y:int):
    f.up()
    f.goto(x,y)
    f.down()
    f.begin_fill()
    f.fillcolor("orange")
    f.seth(280)
    f.fd(100)#
    f.seth(270)
    f.fd(125)#
    f.seth(350)
    f.fd(15)#
    f.seth(240)
    f.fd(28)#
    f.seth(270)
    f.fd(40)#
    f.seth(270)
    f.circle(-20,180)#f.fd(30)
    f.seth(90)
    f.fd(40)#
    f.seth(170)
    f.fd(15)#
    f.seth(60)
    f.fd(28)#
    f.seth(90)
    f.fd(50)#
    for i in range(5):
        f.seth(370)#
        f.circle(10,70)
        f.seth(180)
        f.fd(8)
        f.seth(90)
        f.fd(2)
    f.seth(90)
    f.fd(20)
    f.goto(x,y)
    f.end_fill()

f.speed(1)
drawF(-750,200)
f.speed(0)
drawR(-575,200)
drawE(-390,200)
drawE(-220,200)
drawF(50,200)
drawI(275,200)
drawR(375,200)
drawE(560,200)

f.hideturtle()
while(1):
    f.up()
    f.circle(1)