import turtle

turtle.width(10)

turtle.color("blue")
turtle.circle(50)

turtle.color("black")
turtle.penup() # 抬笔，路径就不坐画出来
turtle.goto(120,0)
turtle.pendown()
turtle.circle(50)

turtle.color("red")
turtle.penup() # 抬笔，路径就不坐画出来
turtle.goto(240,0)
turtle.pendown()
turtle.circle(50)

turtle.color("yellow")
turtle.penup() # 抬笔，路径就不坐画出来
turtle.goto(60,-50)
turtle.pendown()
turtle.circle(50)

turtle.color("green")
turtle.penup() # 抬笔，路径就不坐画出来
turtle.goto(180,-50)
turtle.pendown()
turtle.circle(50)
