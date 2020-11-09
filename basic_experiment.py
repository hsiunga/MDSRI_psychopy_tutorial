# !/usr/bin/env python3.7
# psychopy version 2020.2.4.post1

# exercises for getting started with PsychoPy
# created 10.15.2020 by AH

# import libraries
import os
from psychopy import visual, data, logging, event, core
import numpy as np
import experiment_objects


# functions used in experiment
# def button_placement:
#
#
# def trial_type: (self vs. charity)
#
#
# def trial_type_cond2: (alone vs. watched)
#
#
# def feedback: (display feedback)


# function that starts entire experiment
def main():

    # Store info about the experiment session
    participant_no = input('Participant Number:')
    session_no = input('Session Number:')
    input('Press enter when you are ready to start the task.')
    participant = experiment_objects.Participant(participant_no, session_no)


    # set up file creation
    filename = "[set up path the file creation].csv"
    file_writer = open(filename, 'a')
    file_writer.write('all of your columns aka variables, \n')

    # set up display


    # set up instructions


    # set up recurring images, messages, etc.


    # create trial loop
    # for i in range(total_trials):
    #     trial_object = experiment_objects.OverallTrial()
    #     x = "do all of the things you need"
    #
    #
    #     # write each trial to the csv
    #     file_writer.write(participant.csv_format() + trial_object.csv_format() + '\n')


    # flush and close file when trial loop is finished
    file_writer.flush()
    file_writer.close()

# calls the experiment
if __name__ == '__main__':
    main()