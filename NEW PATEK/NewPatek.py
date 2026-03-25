import tkinter as tk
import math
import time

width = 400
height = 400
center_x = width // 2
center_y = height // 2
radius = 90

bg_color = "#646464"
clock_color = "#e5e7eb"
hour_color = "#ffde57"
min_color = "#343434"
sec_color = "#4584b6"

root = tk.Tk()
root.title("New Patek")
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

        canvas.create_line (x1, y1, x2, y2, fill=clock_color, width=3)

from PIL import Image, ImageTk

img = Image.open("Patek.png")
img = img.resize((400, 400))
bg_img = ImageTk.PhotoImage(img)

canvas.create_image(center_x, center_y, image=bg_img)
canvas.bg_img = bg_img

def draw_hands():
    canvas.delete("hands")

    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(minute * 6 + sec * 0.1)
    hour_angle = math.radians(hour * 30 + minute * 0.5)

    sec_x = center_x + (radius - 20) * math.sin(sec_angle)
    sec_y = center_y - (radius - 20) * math.cos(sec_angle)
    canvas.create_line(center_x, center_y, sec_x, sec_y, fill=sec_color, width=2, tags="hands")
    
    min_x = center_x + (radius - 40) * math.sin(min_angle)
    min_y = center_y - (radius - 40) * math.cos(min_angle)
    canvas.create_line(center_x, center_y, min_x, min_y, fill=min_color, width=4, tags="hands")

    hour_x = center_x + (radius - 70) * math.sin(hour_angle)
    hour_y = center_y - (radius - 70) * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill=hour_color, width=6, tags="hands")


    canvas.create_oval(center_x-5, center_x+5, center_y+5, center_y-5, fill=clock_color, tags="hands")

    root.after(1000, draw_hands)



draw_clock_face()
draw_hands()
root.mainloop()
    
