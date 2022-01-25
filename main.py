from turtle import Turtle,Screen

draw=Turtle()
#triange 360/3
draw.color("green")
draw.forward(100)
draw.right(120)
draw.forward(100)
draw.right(120)
draw.forward(100)
draw.right(120)
draw.forward(100)

#square 360/4 
draw.color("purple")
draw.right(90)
draw.forward(100)
draw.right(90)
draw.forward(100)
draw.right(90)
draw.forward(100)
draw.right(90)
draw.forward(100)

#pentagon 360/5
draw.color("coral")
draw.right(72)
draw.forward(100)
draw.right(72)
draw.forward(100)
draw.right(72)
draw.forward(100)
draw.right(72)
draw.forward(100)
draw.right(72)
draw.forward(100)

#hexagon 360/6
draw.color("orange")
draw.right(60)
draw.forward(100)
draw.right(60)
draw.forward(100)
draw.right(60)
draw.forward(100)
draw.right(60)
draw.forward(100)
draw.right(60)
draw.forward(100)
draw.right(60)
draw.forward(100)

#heptagon 360/7
draw.color("maroon")
draw.right(51.4)
draw.forward(100)
draw.right(51.4)
draw.forward(100)
draw.right(51.4)
draw.forward(100)
draw.right(51.4)
draw.forward(100)
draw.right(51.4)
draw.forward(100)
draw.right(51.4)
draw.forward(100)
draw.right(51.4)
draw.forward(100)

#octagon 360/8
for _ in range (8):
 draw.color("brown")
 draw.right(45)
 draw.forward(100)

 #nonagon 360/9
for _ in range(9):
  draw.color("red")
  draw.right(40)
  draw.forward(100)

#decagon 360/10
for _ in range(10):
  draw.color("blue")
  draw.right(36)
  draw.forward(100)

screen=Screen()
screen.exitonclick()

#Another short method 

from turtle import Turtle,Screen
import random

tim=Turtle()
screen=Screen()
colours=["red","green","blue","orange","purple","maroon","brown","yellow","dark pink","sky blue"]


def draw_shape(num_sides):
  angle = 360/num_sides
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

for shape_side_n in range(3,11):
  tim.color(random.choice(colours))
  draw_shape(shape_side_n)

screen.exitonclick()