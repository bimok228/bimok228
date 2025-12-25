"""
import tkinter as tk
def move_by_keys(event):
    info_coords = canvas.coords(oval)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + " " + str(y))
    if event.keysym == "Up":
        canvas.move(oval, 0, -20)
    elif event.keysym == "Down":
        canvas.move(oval, 0, 20)
    elif event.keysym == "Left":
        canvas.move(oval, -20, 0)
    elif event.keysym == "Right":
        canvas.move(oval, 20, 0)


win = tk.Tk()
label = tk.Label(win, text="INGINIRIUM")
label.pack()
canvas = tk.Canvas(win, bg="#fff", width=700, height=700)
oval = canvas.create_oval((300, 300), (400, 400), fill="yellow")
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()
"""
import tkinter
import random
from tkinter import PhotoImage

def prepare_and_start():
    global player

    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image(
        (player_pos[0], player_pos[1]), image=player_pic, anchor="nw")
    label.config(text="найди выход")
    master.bind("<KeyPress>", key_pressed)
def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[0] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[0] <= 0:
        canvas.move(obj, 0, -HEIGHT)


def key_pressed(event):
    if event.keysym == "Up":
        move_wrap(player, 0, -step)
    elif event.keysym == "Down":
        move_wrap(player, 0, step)
    elif event.keysym == "Right":
        move_wrap(player, step, 0)
    elif event.keysym == "Left":
        move_wrap(player, -step, 0)
master = tkinter.Tk()

step = 32
N_X = 10
N_Y = 10
WIDTH = step * N_X
HEIGHT = step * N_Y
a = False
player_pic = tkinter.PhotoImage(file=r"spritepaint (4).png")

canvas = tkinter.Canvas(master, bg="#FCAB08",
                        width=WIDTH, height=HEIGHT)

player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
print(player_pos)
label = tkinter.Label(master, text="Не попадись!")
restart = tkinter.Button(master, text="Начать занаво",
                         command=prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind("<KeyPress>", key_pressed)
master.mainloop()

