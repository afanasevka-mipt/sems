import turtle as tr
tr.shape('turtle')
tr.color('black', 'yellow')
tr.begin_fill()
for i in range(1, 361):
    tr.forward(1.5)
    tr.left(1)
tr.end_fill()
tr.penup()
tr.goto(-30, 110)
tr.pendown()
def eye():
    tr.color('black', 'blue')
    tr.begin_fill()
    for i in range(1, 361):
        tr.forward(0.3)
        tr.left(1)
    tr.end_fill()
eye()
tr.penup()
tr.goto(30, 110)
tr.pendown()
eye()
tr.penup()
tr.goto(0, 100)
tr.pendown()
tr.right(90)
tr.width(7)
tr.forward(20)
tr.penup()
tr.goto(-30, 60)
tr.pendown()
tr.color('red')
for i in range(1, 181):
    tr.forward(0.5)
    tr.left(1)
tr.done()
