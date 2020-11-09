# !/usr/bin/env python3.7
# psychopy version 2020.2.4.post1

# exercises for getting started with PsychoPy
# created 10.22.2020 by AH

# import libraries
import os
from psychopy import visual, data, logging, event, core
import numpy as np

# Build screen for displaying stimuli
win = visual.Window(size=(1440, 900), fullscr=True, screen=0,
                        allowGUI=False, allowStencil=False, monitor='testMonitor',
                        color='gray', colorSpace='rgb', blendMode='avg', useFBO=True)

# some potentially helpful tricks
blank_fixation = visual.TextStim(win, text='+', color=u'white')  # a fixation cross
globalClock = core.MonotonicClock()  # a global time keeper
trial_clock = core.Clock()  # a trial time keeper (hint: look to the core.Clock.reset to help computer RT's)

# Create a simple trial where the participant sees a shape and has to judge if it has more than 4 sides.
# Print your collected responses (choice and RT) to the terminal.
shape = "Your answer here"
judgement = "Your answer here"

# Create a trial where participants see an image and then rate on a scale of 1 - 5 how pretty they think the image is.
# Print your image name and the collected responses (choice and RT) to the terminal.

path_to_brain = "/Users/abigailhsiung/Documents/Duke/Mentorship/DSRI/psychopy_tutorial/brain.jpg"
img = visual.ImageStim(win, image=path_to_brain, size=[0.4, 0.5], pos=[0, 0.2])
rating_scale = visual.RatingScale(win, singleClick=True)

blank_fixation.draw()
win.flip()
core.wait(2)

while rating_scale.noResponse:
    img.draw()
    rating_scale.draw()
    win.flip()

rating = rating_scale.getRating()
decision_time = rating_scale.getRT()
print(rating, decision_time)

core.wait(0.5)

if not rating_scale.noResponse:
    blank_fixation.draw()
    win.flip()
    core.wait(2)
    win.close()



# Create a trial where participants see an image and if they respond with the left arrow key, they receive positive feedback and
# if they respond with the right arrow key they receive negative feedback. (Hint: try to great a function with a conditional statement)
# Print image name and responses (choice and RT) to terminal.

# sample function
def feedback(choice):
    if choice == "??":
        display = "positive"
    else:
        display = "negative"

# Create a trial where participants see two images and select which one they find most appealing. Their selection will bring up
# a different set of two images that they will make a second choice on (much like the two-stage choice task we talked about in lecture).
# Randomize the order of which image appears on the left and which appears on the right
# (Hint: you can use some of the same functionality from your feedback function to create a new function)
# Print both image names and the response chosen (choice and RT) for each step in the trial to the terminal.

# sample randomizer
def img_position():
    val = np.random.randint(2, size=1)
    if val == 1:
        xdelta = 0.5 # this value gives you a position (an x-coordinate) that you can work with to change where the image is placed
    else:
        xdelta = -0.5 # you want the opposing one to make sure your images are evenly placed on the screen
    return xdelta

# function that takes the img_position output and uses it to determine image display
def display_images(win): # takes parameter of your window
    xdelta = img_position()

    # assign images a position
    img_1 = "Your answer here"
    img_2 = "Your answer here"

    # make note of which image is placed on which side
    if xdelta < 0:
        side = "Your answer here"
    else:
        side = "Your answer here"
    return img_1, img_2

