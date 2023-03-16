import turtle

tao = turtle.Pen()
tao.shape('turtle')


default = -300
taoposix = default
taoposiy = default

tao.speed(0)
tao.pensize(5)
tao.penup()
tao.goto(default,default)
tao.pendown()

for k in range(5):
    for j in range(5):
        for i in range(6):
            tao.forward(50)
            tao.left(60)
            
        tao.penup()
        taoposix+=100
        tao.goto(taoposix, taoposiy)
        tao.pendown()

    taoposix = default
    tao.penup()
    taoposiy+=85
    tao.goto(taoposix, taoposiy)
    tao.pendown()

turtle.done()