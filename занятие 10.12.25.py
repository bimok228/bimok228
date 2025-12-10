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
"""
import tkinter as tk

def move_by_keys(event):
    if event.keysym == "Up":
        canvas.move(oval, 0, -20)
    elif event.keysym == "Down":
        canvas.move(oval, 0, 20)
    elif event.keysym == "Left":
        canvas.move(oval,-20, 0)
    elif event.keysym == "Left":
        canvas.move(oval, 20, 0)
win.tk.Tk()
label = tk.Label(win, text="IGINIRIYM")
label.pack()
canvas = tk.Canvas(win, bg="#fff", width=700, height=700)
oval = canvas.create_oval((300, 300), (400, 400), fill="yellow")
canvas.pack()
win.bind("<kevPress>". move by kevs)