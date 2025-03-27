import turtle
from xml.sax.handler import property_xml_string

t=turtle.Turtle()
t.shapesize(3)
t.shape("turtle")
t. color("blue","green")
t.speed(1)
screen=turtle.Screen()
screen.screensize(800,500,"lightblue")

#grass
t.color("green")
t.begin_fill()
t.forward(1270)
t.right(90)
t.fd(720)
t.rt(90)
t.fd(2550)
t.rt(90)
t.fd(720)
t.rt(90)
t.fd(1270)
t.end_fill()

#house
t.penup()
t.goto(-300.00,250.00)
t.pd()
t.color("grey")
t.begin_fill()
t.lt(180)
t.fd(600.00)
t.lt(90.00)
t.fd(600.00)
t.lt(90)
t.fd(600.00)
t.lt(90)
t.fd(600.00)
t.end_fill()
















turtle.exitonclick()
