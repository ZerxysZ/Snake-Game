# Snake Game

import turtle
import time
import random

delay = 0.15

# Screen
wn = turtle.Screen()
wn.title("Snake Game By Zerxys")
wn.bgcolor("Purple")
wn.setup(width=600, height=600)
wn.tracer(0) #Turns off the screen updates btw

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Bussin or NOT?
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0,100)

segements = []




#Functions 
def go_up():
    if head.direction != "down":
    head.direction = "up"

    def go_down():
        if head.direction != "up":
    head.direction = "down"

    def go_left():
        if head.direction != "right":
    head.direction = "left"

    def go_right():
        if head.direction != "left":
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

  if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

  if head.direction == "left":
        y = head.xcor()
        head.setx(x - 20)

  if head.direction == "right":
        y = head.xcor()
        head.setx(x - 20)

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True: 
    wn.update()
# check for collision with the border
if head.xcor() >290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

# Hide segments
for segment in segements:
    segement.goto(1000, 1000)

# Clear the segments list
segements.clear()

# Collision for food
if head.distance(food) < 20:
    # Move food to a random spot
x = random.randint(-290, 290)
y = random.randint(-290, 290)
food.goto(x,y)

# Add a segment
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segements.append(new_segment)

# mOVE END SEGMENT FIRST IN REVERSE ORDER
for index in range(len(segments)-1, 0, -1):
    x = segements[index-1].xcor()
    y = segements[index-1].ycor()
    segements[index].goto(x, y)
    
    # Move segment 0 to head
    if len(segements) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)



    move()

    # Check for head collisions with the body segments
    for segment in segements:
        if segmement.distance(head) < 20:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
# Hide segments
for segment in segements:
    segement.goto(1000, 1000)

# Clear the segments list
    segements.clear()
    
    
time.sleep(delay)

wn.mainloop()

