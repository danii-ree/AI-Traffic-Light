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

# Creating a  canvas for 
myCanvas = Canvas(root)
myCanvas.pack()

# function for creating a circle
def CreateCircle(x, y, r, canvas, fillColor = "black"):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=fillColor)
def lightsOff():
    CreateCircle(190, 120, 20, myCanvas, "black")
    CreateCircle(190, 160, 20, myCanvas, "black")
    CreateCircle(190, 200, 20, myCanvas, "black")
# STILL WORKING ON IT
def redLight():
    global red, yellow, green
    red = True
    yellow = False 
    green = False

    if red == True: 
        CreateCircle(190, 120, 20, myCanvas, "red")
        red = False
    elif red == False: 
        myCanvas.delete('all')
def yellowLight():
    global red, yellow, green
    red = False
    yellow = True 
    green = False

    print(red)
    if yellow == True: 
        CreateCircle(190, 160, 20, myCanvas, "yellow")
    else: 
        CreateCircle(190, 160, 20, myCanvas, "black")
def greenLight():
    global red, yellow, green
    red = False
    yellow = False 
    green = True

    if green == True: 
        CreateCircle(190, 200, 20, myCanvas, "green")
    else: 
        CreateCircle(190, 200, 20, myCanvas, "black")

lightsOff()

# setting up the buttons - Red, Yellow, Green is needed to light up traffic lights
redButton = Button(root, text="Red", command=redLight)
redButton.pack(side="left", padx=20)

yellowButton = Button(root, text="Yellow", command=yellowLight)
yellowButton.pack(side="left", padx=80)

greenButton = Button(root, text="Green", command=greenLight)
greenButton.pack(side="right", padx=30)


root.mainloop()