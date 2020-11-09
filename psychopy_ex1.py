# !/usr/bin/env python3.7
# psychopy version 2020.2.4.post1

# exercises for getting started with PsychoPy
# created 10.15.2020 by AH

# import libraries
import os
from psychopy import visual, data, logging, event, core
import numpy as np

# Exercise 1: create experiment window:

# win = visual.Window(size=(800,800))
# # win = visual.Window(size=(1440, 900)), #fullscr=True, screen=0,
# #                         allowGUI=False, allowStencil=False, monitor='testMonitor',
# #                         color='grey', colorSpace='rgb', blendMode='avg', useFBO=True)
#
# # msg = visual.TextStim(win, text="Hello World")
# # msg.draw()
# # # To help you not get stuck in a screen
# win.flip() # updates the experiment window
# core.wait(2) # waits for a second
# win.close() # closes the experiment window
#
# # Exercise 1.1: Change the color of the background to grey and make the size full screen:
win2 = visual.Window(size=(1440, 900), fullscr=True, screen=0,
                        allowGUI=False, allowStencil=False, monitor='testMonitor',
                        color='gray', colorSpace='rgb', blendMode='avg', useFBO=True)
#
# msg = visual.TextStim(win2, text="Happy Friday")
#
# msg.draw()
# win2.flip()
# core.wait(2)
# win2.close()
#
# # # Exercise 2: Display "Hello World" on your window
msg = "Your message here!"
#
# # You will also need a built-in function that will actually display your msg on your window
# # [built-in function here]
#
# win2.flip()
# core.wait(2)
# win2.close()
#
# # Exercise 3: Display a circle
# cir = visual.Circle(win2, radius=0.5, fillColor='blue')
# # You will also need a built-in function that will actually display your msg on your window
# # [built-in function here]
#
# cir.draw()
# win2.flip()
# core.wait(2)
# win2.close()
#
# # Exercise 3.1: Change the color of the circle (both the outside line and the fill color). Change the opacity of the circle to 0.6 and move it to the upper right hand corner.
# cir2 = "Your answer here!"
#
# # You will also need a built-in function that will actually display your msg on your window
# # [built-in function here]
#
# win2.flip()
# core.wait(2)
# win2.close()
#
# # Exercise 4: Display a circle with Hello World written overtop of it
# cir3 = "Your answer here"
# msg2 = "Your answer here"
#
# # [built-in function here]
# # [built-in function here]
#
# win2.flip()
# core.wait(2)
# win2.close()
#
# # Exercise 5: Display an image and make it disappear when you click "Enter"
# # You will need to tell your program where it can find the image!
path_to_brain = "/Users/abigailhsiung/Documents/Duke/Mentorship/DSRI/psychopy_tutorial/brain.jpg"
img = visual.ImageStim(win2, image=path_to_brain)

# You might need to update your window more than once
# [built-in function here]
img.draw()
win2.flip()
press_enter = event.waitKeys(maxWait=10, keyList='return', timeStamped=True)
win2.flip()
core.wait(1)
win2.close()