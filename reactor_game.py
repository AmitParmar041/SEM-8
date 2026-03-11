import tkinter as tk
import random
import math

# -----------------------
# GAME VARIABLES
# -----------------------

heat = 0
power = 0
rods = 10
steam = 40
demand = random.randint(800,1500)
score = 0
money = 1000
angle = 0

running = True

# -----------------------
# REACTOR LOGIC
# -----------------------

def update_reactor():

    global heat,power,demand,score,money

    if not running:
        return

    heat = rods * 6
    power = rods * steam

    canvas.delete("all")

    draw_gauge(heat,200,120,120,"HEAT")
    draw_gauge(power,2000,380,120,"POWER")

    canvas.create_text(
        250,
        230,
        text=f"City Demand: {demand}",
        fill="white",
        font=("Arial",14)
    )

    if abs(power - demand) < 80:
        score += 5
        money += 20

    if random.randint(1,6)==1:
        demand=random.randint(800,1500)

    score_label.config(text=f"Score: {score}")
    money_label.config(text=f"Money: ${money}")

    if heat > 180:
        meltdown()
        return

    animate_turbine()

    root.after(1000,update_reactor)

# -----------------------
# GAUGE
# -----------------------

def draw_gauge(value,max_value,x,y,label):

    canvas.create_oval(x-70,y-70,x+70,y+70,outline="white",width=2)

    angle = (value/max_value)*180
    rad = math.radians(angle-90)

    nx = x + 60*math.cos(rad)
    ny = y + 60*math.sin(rad)

    canvas.create_line(x,y,nx,ny,width=3,fill="red")

    canvas.create_text(x,y+80,text=label,fill="white")

# -----------------------
# TURBINE ANIMATION
# -----------------------

def animate_turbine():

    global angle

    cx = 250
    cy = 320

    size = 40

    for i in range(4):

        a = math.radians(angle + i*90)

        x = cx + size*math.cos(a)
        y = cy + size*math.sin(a)

        canvas.create_line(cx,cy,x,y,fill="cyan",width=3)

    angle += power/100

# -----------------------
# MELTDOWN
# -----------------------

def meltdown():

    canvas.delete("all")

    canvas.create_text(
        250,
        200,
        text="💥 REACTOR MELTDOWN 💥",
        fill="red",
        font=("Arial",26)
    )

# -----------------------
# CONTROL KNOBS
# -----------------------

def increase_rods():
    global rods
    if rods < 30:
        rods += 1

def decrease_rods():
    global rods
    if rods > 0:
        rods -= 1

def increase_steam():
    global steam
    if steam < 100:
        steam += 5

def decrease_steam():
    global steam
    if steam > 0:
        steam -= 5

# -----------------------
# UI
# -----------------------

root = tk.Tk()
root.title("Reactor Simulator V5")
root.geometry("500x500")
root.configure(bg="black")

canvas = tk.Canvas(
    root,
    width=500,
    height=380,
    bg="black",
    highlightthickness=0
)

canvas.pack()

control_frame = tk.Frame(root,bg="black")
control_frame.pack()

tk.Button(
    control_frame,
    text="Rods +",
    command=increase_rods
).grid(row=0,column=0,padx=10)

tk.Button(
    control_frame,
    text="Rods -",
    command=decrease_rods
).grid(row=0,column=1,padx=10)

tk.Button(
    control_frame,
    text="Steam +",
    command=increase_steam
).grid(row=0,column=2,padx=10)

tk.Button(
    control_frame,
    text="Steam -",
    command=decrease_steam
).grid(row=0,column=3,padx=10)

score_label = tk.Label(
    root,
    text="Score: 0",
    fg="white",
    bg="black"
)

score_label.pack()

money_label = tk.Label(
    root,
    text="Money: $1000",
    fg="white",
    bg="black"
)

money_label.pack()

update_reactor()

root.mainloop()