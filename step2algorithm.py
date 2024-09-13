import turtle as trtl

t = trtl.Turtle()

screen = trtl.Screen()
screen.setup(width=800, height=600) 

def drawSq(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def putObj(numObj):
      
    spacing = (800 - numObj * 50) / (numObj + 1)
    
    start_x = -(800 / 2) + spacing + (50 / 2)
    y=0

    t.penup()
    
    for j in range(numObj):
        t.goto(start_x + j * (50 + spacing), y)
        t.pendown()
        drawSq(t, 50)
        t.penup()

    t.hideturtle()

userInput = int(input("How many objects do you want?"))
putObj(userInput)

wn = trtl.Screen()
wn.mainloop()
