import time
import turtle as tt

tt.title("NullFullZero")
tt.pencolor("red")
tt.pensize(1)

tt.penup()
tt.goto(-100,100)
tt.pendown()

for i in range(30):
    tt.forward(90)
    tt.right(70)
    time.sleep(0.1)

tt.goto(-100,100)

tt.penup()
tt.goto(-100,300)
tt.pencolor("grey")
tt.pendown()

for i in range(30):
    tt.forward(70+i)
    tt.right(90+i)
    time.sleep(0.1)

tt.penup()
tt.goto(-100,-300)
tt.pencolor("blue")
tt.pendown()


for i in range(10):
    tt.forward(70*(i/4))
    tt.right(90)
    time.sleep(0.1)

tt.mainloop()