import turtle 
window = turtle.Screen()

#stem
pen = turtle.Turtle()
pen.up()
pen.speed(1)
pen.down()
pen.back(10)
pen.right(90)
pen.down()
pen.forward(112.5)
pen.right(135)

#leaf 1
pen.circle(60, 90)
pen.left(90)
pen.circle(60, 90)
pen.right(135)
pen.forward(87.5)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(150)
pen.left(225)

#leaf 2
pen.circle(60, 90)
pen.left(90)
pen.circle(60, 90)
pen.right(135)
pen.forward(50)
pen.left(90)
pen.forward(10)

#spacing 
pen.up()
pen.right(90)
pen.forward(65)
pen.right(90)
pen.back(15)

pen.down()

#first layer of flower

for i in range(8):
    pen.circle(40, 180)
    pen.left(45)

pen.up()
pen.right(90)
pen.forward(20)
pen.left(90)
pen.back(64)
pen.right(90)
pen.back(93)

pen.down()

#second layer of flower 

for j in range(8):
    pen.circle(80, 180)
    pen.left(45)