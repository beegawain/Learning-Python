import turtle
turtle.screensize(1024,768)
turtle.write("Hello",font=("宋体",20,"normal"))
turtle.showturtle()     #显示

turtle.begin_fill()
turtle.circle(50)
turtle.color("red")
turtle.end_fill()

turtle.done()