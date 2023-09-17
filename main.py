"""
THE TRAFFIC AI CODE.
****************************
This is simply a simulator, but it could definitely be used in real life. We can implement this either by using an 
Arduino or a traffic light circuit.
"""
from tkinter import * 

# intiallizing all the necessary components (root, width, height, title, etc.)
root = Tk()
root.title("Traffic Light Simulator")
width = 400
height = 600
root.geometry(f'{width}x{height}')

red = False
yellow = False
green = False

lightColor = "black"

# Creating a  canvas for 
myCanvas = Canvas(root)
myCanvas.pack()

# STILL WORKING ON IT
# def redButton(lightSwitch):
#     print("Red Button is working")
#     red = True
#     if red == True:
#         lightSwitch = "red"

# function for creating a circle
def CreateCircle(x, y, r, canvas, fillColor = lightColor):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=fillColor)

CreateCircle(190, 120, 20, myCanvas)
CreateCircle(190, 160, 20, myCanvas)
CreateCircle(190, 200, 20, myCanvas)

# setting up the buttons - Red, Yellow, Green is needed to light up traffic lights
redButton = Button(root, text="Red", command=redButton(lightColor))
redButton.pack(side="left", padx=20)

yellowButton = Button(root, text="Yellow")
yellowButton.pack(side="left", padx=80)

greenButton = Button(root, text="Green")
greenButton.pack(side="right", padx=30)


root.mainloop()