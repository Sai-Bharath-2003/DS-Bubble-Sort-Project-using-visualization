#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Bubble Sort Code
import time
def bubble(inputv, datadraw, timer):
# inputv is passed for the set of unsorted inputed data values
# datadraw is used to generate the data bars in the visualizationf
# timer iis for the speed range
    n = len(inputv)
    for i in range(n):
        for j in range(0, n-i-1):
            if inputv[j] > inputv[j+1]:
                inputv[j], inputv[j+1] = inputv[j+1], inputv[j]
                # if swapped then color becomes Green else stays Red
                datadraw(inputv, ['SteelBlue1' if x == j +
                                1 else 'firebrick1' for x in range(len(inputv))])
                time.sleep(timer)
    # sorted elements generated with Green color
    datadraw(inputv, ['medium spring green' for x in range(len(inputv))])


# In[ ]:


from tkinter import *
from tkinter import ttk
import random
# initialising root class for Tkinter
root = Tk()
root.title("Bubble Sort Visualizer")
# window size
root.maxsize(900, 600)
root.config(bg="Black")
inputv = []
 
# A function to generate the data values  
def generate():
    global inputv
    min_val = int(minEntry.get())
#   minimum value of the range 
 
    max_val = int(maxEntry.get())
#   maximum value of the range
 
    sizeval = int(sizeEntry.get())
#   number of data values/bars to be generated
 
#   creating a list blank data  which will be filled with random data values further
    inputv = []
    for _ in range(sizeval):
        inputv.append(random.randrange(min_val, max_val+1))
    drawData(inputv, ['firebrick1' for x in range(len(inputv))])

# A function to create the data bars by creating a canvas in Tkinter
def drawData(inputv, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width/(len(inputv) + 1)
    offset = 30
    spacing = 10

    normalized_data = [i / max(inputv) for i in inputv] 
# normalizing data for rescaling real-valued numeric data within the given range

    for i, height in enumerate(normalized_data):
        # top left corner
        x0 = i*x_width + offset + spacing
        y0 = can_height - height*340
 
        # bottom right corner
        x1 = ((i+1)*x_width) + offset
        y1 = can_height
 
        # data bars are generated as Red colored vertical rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SE, text=str(inputv[i]))
    root.update_idletasks()

# function to initiate the sorting process by calling the extension code
def start_algorithm():
    global inputv
    bubble(inputv, drawData, speedbar.get())
 
 
# creating main user interface frame 
Mainframe = Frame(root, width=600, height=200, bg="black")
Mainframe.grid(row=0, column=0, padx=10, pady=5)
 
canvas = Canvas(root, width=600, height=380, bg="old lace")
canvas.grid(row=1, column=0, padx=10, pady=5)
 
# creating user interface area in grid manner
# first row components
Label(Mainframe, text=" BUBBLE  SORT  ALGORITHM ", bg='ghostwhite').grid(
    row=0, column=1, padx=5, pady=5, sticky=W)
 
# creating Start Button to start the sorting visualization process
Button(Mainframe, text="START", bg="ghostwhite", command=start_algorithm).grid(
    row=1, column=3, padx=5, pady=5)
 
# creating Speed Bar using scale in Tkinter
speedbar = Scale(Mainframe, from_=0.10, to=2.0, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)
 
# second row components
# sizeEntry : scale to select the size/number of data bars
sizeEntry = Scale(Mainframe, from_=3, to=20, resolution=1,
                  orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)
 
# minEntry : scale to select the minimum value of data bars
minEntry = Scale(Mainframe, from_=0, to=10, resolution=1,
                 orient=HORIZONTAL, label="Minimum Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)
 
# maxEntry : scale to select the maximum value of data bars
maxEntry = Scale(Mainframe, from_=10, to=50, resolution=1,
                 orient=HORIZONTAL, label="Maximum Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# creating generate button
Button(Mainframe, text="Generate", bg="ghostwhite", command=generate).grid(
    row=0, column=3, padx=5, pady=5)
 
# to stop automatic window termination
root.mainloop()


# In[ ]:




