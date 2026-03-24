import tkinter as tk
import math
import time

width = 400
height = 400
center_x = width // 2
center_y = height // 2
radius = 150

bg_color = "#646464"
clock_color = "#e5e7eb"
hour_color = "#ffde57"
min_color = "#343434"
sec_color = "#4584b6"

root = tk.Tk()
root.title("WatchWatch")
canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
canvas.pack()


def draw_clock_face():
    canvas.create_oval(
        center_x - radius,
        center_y - radius, 
        center_x + radius, 
        center_y + radius, 
        outline = clock_color, 
        width=4
    )

    for i in range(12):
        angle = math.radians(i * 30)
        x1 = center_x + (radius - 10) * math.sin(angle)
        y1 = center_y - (radius - 10) * math.cos(angle)
        x2 = center_x + radius * math.sin(angle)
        y2 = center_x - radius * math.cos(angle)

        canvas.create_line (x1, y2, x2, y2, fill=clock_color, width=3)

def draw_hands():

draw_clock_face
root.mainloop()
    
