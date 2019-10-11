import turtle

t=turtle.Pen()
color=("red","yellow","black","pink","green")
t.width(4)
t.speed(0)

for i in range(100):
    t.penup()
    t.goto(0,-i*2)            #0,-100,-200,-300,-400
    t.pendown()
    t.color(color[i%len(color)])
    t.circle(2*i+4)

turtle.done()