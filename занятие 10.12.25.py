"""
import tkinter as tk
win = tk.Tk()
canvas = tk.Canvas(win, bg="Green", width = 1980, height = 1080)
# bg - backgraud
canvas.pack()
win.mainloop()

import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg="#off", width = 700, height = 700)
canvas.create_oval((300, 300), (500, 500), fill="yellow")
canvas.create_line((0, 0), (100, 200), (300, 300), (200, 100), (0, 0), fill="black")
canvas.pack()
win.mainloop()

import tkinter as tk

def move_by_keys(event):
    if event.keysym == "Up":
        canvas.move(oval, 0, -20)
    elif event.keysym == "Down":
        canvas.move(oval, 0, 20)
    elif event.keysym == "Left":
        canvas.move(oval, -20, 0)
    elif event.keysym == "Right":
        canvas.move(oval, 20, 0)
win = tk.Tk()
label = tk.Label(win, text="IGINIRIYM")
label.pack()
canvas = tk.Canvas(win, bg="#fff", width=400, height=400)
oval = canvas.create_oval((300, 300), (400, 400), fill="yellow")
canvas.create_line((0, 0), (0, 400), (100, 0), (1, 100), (0, 0), fill="black")
canvas.create_line(300, 0) fill="black"))
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()
import tkinter

size, amount = 400,8
master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg="white", height=size, width=size)
for x in range(0, size, size)
canvas.pack()
win.mainloop()
"""