from turtle import * 
#drawing a square

shape("turtle")
speed(30)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

#end of square

left(90)
forward(70)

#drawing a door

color("blue")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#end of drawing a door

penup()
goto(200, 200)
pendown()


color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of drawing a roof

penup()
goto(180, 180)
pendown()

#drawing right window 

color("brown")
begin_fill()
left(30)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#end of drawing right window 

penup()
goto(20, 180)
pendown()

#drawing left window
 
begin_fill() 
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#end of drawing left window 








exitonclick()