from turtle import *
colors = ['purple','pink']
pencolor('beige')
pensize (3)
for i in range (6,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()
