"""
THIS IS THE TRAFFIC AI CODE. 
"""
from tkinter import * 

# intiallizing all the necessary components (root, width, height, title, etc.)
root = Tk()
root.title("Traffic Light Simulator")
width = 400
height = 600
root.geometry(f'{width}x{height}')

myCanvas = Canvas(root)
myCanvas.pack()

def CreateCircle(x, y, r, canvas):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1)

CreateCircle(150, 220, 20, myCanvas)

# setting up the buttons - Red, Yellow, Green is needed to light up traffic lights
redButton = Button(root, text="Red")
redButton.pack(side="left", padx=20)

yellowButton = Button(root, text="Yellow")
yellowButton.pack(side="left", padx=80)

greenButton = Button(root, text="Green")
greenButton.pack(side="right", padx=30)


root.mainloop()