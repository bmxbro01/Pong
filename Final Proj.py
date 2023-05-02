# Project By Zack And Danial
# Pong
import random
import traceback
from tkinter import *

# Window setup
root = Tk()
root.title('Pong')
canvas = Canvas(root, width=800, height=800, bg="skyblue")

# Random speed and scoring
x_speed = random.randint(3, 8)
y_speed = random.randint(3, 8)
score = 0
escore = 0

# Creates objects
bob = canvas.create_rectangle(50, 20, 70, 90, fill="black")
e_bob = canvas.create_rectangle(720, 620, 740, 690, fill="black")
ball = canvas.create_oval(390, 390, 390 + 30, 390 + 30, fill='black', outline='black')

# Input for file
file = input("Enter file name: ")
players = input("Enter player 1,2: ")
names = players.split(",")
player1 = names[0]
player2 = names[1]


# Update position and check for collision
def move_ball():
    global x_speed, y_speed
    global score, escore, ball
    global file, player1, player2

    w, x, y, z = canvas.coords(ball)
    w1, x1, y1, z1 = canvas.coords(bob)
    w2, x2, y2, z2 = canvas.coords(e_bob)

    # Players collision
    if w <= 70 and y >= 50 and (x + 20 >= x1 and z - 20 <= z1):
        x_speed = -x_speed
        overlaps_a = canvas.find_overlapping(w, x, y, z)
        if len(overlaps_a) == 2:
            if ball <= y1 - 2:
                canvas.move(ball, 20, 0)
    if w <= 740 and y >= 720 and (x + 20 >= x2 and z - 20 <= z2):
        x_speed = -x_speed
        overlaps_a = canvas.find_overlapping(w, x, y, z)
        if len(overlaps_a) == 2:
            if ball <= w2 + 2:
                canvas.move(ball, -20, 0)

    # Adds point when hits west and east border and bounces off --- Danny
    if y > 816:
        score += 1
        point.config(text=score)
        x_speed = -x_speed
        try:
            with open(file, 'a') as f:
                f.write(player1 + " " + str(score)+'\n')
        except EXCEPTION:
            print(traceback.format_exc())
    elif y < 16:
        escore += 1
        e_point.config(text=escore)
        x_speed = -x_speed
        try:
            with open(file, 'a') as f:
                f.write(player2 + " " + str(score) + "\n")
        except EXCEPTION:
            print(traceback.format_exc())

    # Starts game over --- Danny
    if score >= 10:
        canvas.delete(ball)
        ball = canvas.create_oval(390, 390, 390 + 30, 390 + 30, fill='black', outline='black')
        try:
            with open(file, 'a') as f:
                f.write(player1.capitalize() + " " + str(score)+" Winner\n")
        except EXCEPTION:
            print(traceback.format_exc())
        score = 0
        escore = 0
        point.config(text=score)
        e_point.config(text=escore)

    # --- Danny
    if escore >= 10:
        canvas.delete(ball)
        ball = canvas.create_oval(390, 390, 390 + 30, 390 + 30, fill='black', outline='black')
        try:
            with open(file, 'a') as f:
                f.write(player2.capitalize() + " " + str(escore) + " Winner\n")
        except EXCEPTION:
            print(traceback.format_exc())
        escore = 0
        score = 0
        point.config(text=score)
        e_point.config(text=escore)

    # Bounce off north and south border
    if x <= 2 or x >= 778:
        y_speed = -y_speed

    canvas.move(ball, x_speed, y_speed)
    canvas.after(30, move_ball)


canvas.after(30, move_ball)


# Player movement
def up(event):
    w, x, y, z = canvas.coords(bob)
    if x > 30:
        canvas.move(bob, 0, -50)


def down(event):
    w, x, y, z = canvas.coords(bob)
    if x < 690:
        canvas.move(bob, 0, 50)


def e_up(event):
    w, x, y, z = canvas.coords(e_bob)
    if x > 30:
        canvas.move(e_bob, 0, -50)


def e_down(event):
    w, x, y, z = canvas.coords(e_bob)
    if x < 690:
        canvas.move(e_bob, 0, 50)


canvas.bind("<w>", up)
canvas.bind("<s>", down)
canvas.bind("<i>", e_up)
canvas.bind("<k>", e_down)

# Scores label
point = Label(root,
              text=score,
              bg='skyblue',
              fg="white",
              font=('Times', 40))
e_point = Label(root,
                text=escore,
                bg='skyblue',
                fg="white",
                font=('Times', 40))

# Label placement and window set up
point.place(x=300, y=30)
e_point.place(x=500, y=30)
canvas.focus_set()
canvas.pack()
root.mainloop()

# todo list
# Spring break Zack worked over 10 hours

# Wednesday danny worked for 3 hours
# Friday danny worked for an hour
# Monday danny worked for 3 hours
# Wednesday danny worked for an hour
# Friday danny worked for 2 hours

# Zack --- 10 hours
# Danny -- 10 hours
