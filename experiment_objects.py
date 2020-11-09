# !/usr/bin/env python3.7
# psychopy version 2020.2.4.post1

# objects for basic experiment with PsychoPy
# created 10.15.2020 by AH

# import libraries
import os


# subject specific parameters
class Participant():

    def __init__(self, id, sesh):
        self.id = id
        self.session = sesh

    def csv_format(self):
        return '{}, {}, '.format(self.id, self.session)


# trial specific parameters
class OverallTrial():

    def __init__(self, trial_no, global_time, category_of_pics, probability, reward_type, majority_cat):
        self.trial_no = trial_no
        self.global_time = global_time
        self.category_type = category_of_pics
        self.prob_dist = probability
        self.reward_type = reward_type
        self.majority_cat = majority_cat
        self.final_choice = None  # indoor, outdoor, living, non
        self.final_choice_time = None
        self.global_final_choice_time = None
        self.samples = []
        self.majority_side = None
        self.num_of_pics_sampled = 0
        self.total_trial_time = None

    def csv_format(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '.format(self.trial_no, self.global_time,
                                                                     self.category_type,
                                                                     self.prob_dist, self.reward_type,
                                                                     self.majority_cat, self.final_choice,
                                                                     self.final_choice_time, self.num_of_pics_sampled,
                                                                     self.global_final_choice_time,
                                                                     self.total_trial_time)


    def set_final_choice(self, final_dir):
        if self.majority_side == final_dir:
            self.final_choice = self.majority_cat
        else:
            self.final_choice = minority_category[self.majority_cat]
