"""
THE TRAFFIC AI CODE.
****************************
This is simply a simulator, but it could definitely be used in real life. We can implement this either by using an 
Arduino or a traffic light circuit.
"""
from tkinter import * 
import customtkinter as ctk
from PIL import ImageTk, Image
from Detection import *

ctk.set_appearance_mode("#f0f0f0")
ctk.set_default_color_theme("blue")

# intiallizing all the necessary components (root, width, height, title, etc.)
root = ctk.CTk()
root.title("Traffic Light Simulator")
width = 600
height = 600
root.geometry(f'{width}x{height}')

global red, yellow, green
red = False
yellow = False
green = False

# Creating a  canvas for traffic lights
myCanvas = Canvas(root, bg="#f0f0f0", borderwidth=0)
myCanvas.pack()

# Images of the traffic light
tflight_bg = Image.open('./Traffic Light Images/tfLight_bg.png')
light_off1 = Image.open('./Traffic Light Images/light_off1.png')
light_off2 = Image.open('./Traffic Light Images/light_off2.png')
light_off3 = Image.open('./Traffic Light Images/light_off3.png')
Red_light = Image.open('./Traffic Light Images/Red.png')
Yellow_light = Image.open('./Traffic Light Images/Yellow.png')
Green_light = Image.open('./Traffic Light Images/Green.png')

tflight_bg = tflight_bg.resize((100, 150))
light_off1 = light_off1.resize((100, 150))
light_off2 = light_off2.resize((100, 150))
light_off3 = light_off3.resize((100, 150))
Red_light = Red_light.resize((100, 150))
Yellow_light = Yellow_light.resize((100, 150))
Green_light = Green_light.resize((100, 150))

test1 = ImageTk.PhotoImage(tflight_bg)
test2 = ImageTk.PhotoImage(light_off1)
test3 = ImageTk.PhotoImage(light_off2)
test4 = ImageTk.PhotoImage(light_off3)
test5 = ImageTk.PhotoImage(Red_light)
test6 = ImageTk.PhotoImage(Yellow_light)
test7 = ImageTk.PhotoImage(Green_light)

myCanvas.create_image(150, 150, image=test1)

def CreateCircle(x, y, r, canvas, fillColor = "black"):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=fillColor)

# functions for turning the lights on or off
def lightsOff():
    myCanvas.create_image(150, 150, image=test2)
    myCanvas.create_image(150, 150, image=test3)
    myCanvas.create_image(150, 150, image=test4)
    
def redLight():
    global red, yellow, green

    if pedestrian_count == 0 and car_count > 0 and yellow == False: 
        if red:
            myCanvas.create_image(150, 150, image=test5)
            red = False
        else:
            myCanvas.create_image(150, 150, image=test2)
            red = True
    
def yellowLight():
    global red, yellow, green

    if pedestrian_count == 0 and car_count > 0 and red == False: 
        if yellow: 
            myCanvas.create_image(150, 150, image=test6)
            yellow = False
        else: 
            myCanvas.create_image(150, 150, image=test3)
            yellow = True
def greenLight():
    global red, yellow, green
    if green: 
        myCanvas.create_image(150, 150, image=test7)
        green = False
    else:
        myCanvas.create_image(150, 150, image=test4)
        green = True

start_video_thread()

lightsOff()

root.mainloop()
