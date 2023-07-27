import time
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("Analog Clock")
wn.tracer(0)

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(100)
pen.pensize(3)

def draw_clock(h,m,s,pen):
  #draw clock face
 pen.up()
 pen.goto(0,210)
 pen.setheading(180)
 pen.color("green")
 pen.pendown()
 pen.circle(210)

 pen.penup()
 pen.goto(0,0)
 pen.setheading(90)

 for i in range(12):
  pen.forward(190)
  pen.pendown()
  pen.forward(20)
  pen.penup()
  pen.goto(0,0)
  pen.right(30)

 pen.penup()
 pen.goto(0,0)
 pen.color("blue")
 pen.setheading(90)
 angle=(h/12)*360
 pen.right(angle)
 pen.pendown()
 pen.forward(120)

 pen.penup()
 pen.goto(0,0)
 pen.color("white")
 pen.setheading(90)
 angle=(m/60)*360
 pen.right(angle)
 pen.pendown()
 pen.forward(160)

 pen.penup()
 pen.goto(0,0)
 pen.color("yellow")
 pen.setheading(90)
 angle=(s/60)*360
 pen.right(angle)
 pen.pendown()
 pen.forward(80)

while True:
 h =int(time.strftime("%I"))
 m =int(time.strftime("%M"))
 s =int(time.strftime("%S"))


 draw_clock(h,m,s,pen)
 wn.update()

 pen.clear()
 time.sleep(1)

wn.mainloop()