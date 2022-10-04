import qe_radar as qe
import example_team_logic as lg
import numpy as np


# Define the time allowed to measure a target
RADAR_WINDOW = 1000

# Apply the token granted to a team so they may use the simulator
qe.set_auth("")


##################################################
######## PHASE ONE - DATA COLLECTION #############
##################################################
# Build a normal map of an example (0-999)
def create_example_map(example):
    
    #start of pulse phase
    pul_start = 0
    #end of pulse phase
    pul_end = 0 + np.random.randint(0,100)
    #start of detection window
    det_start = 0
    #end of detection window
    det_start = det_start + np.random.randint(0, 100)

    #if detection window starts at TOTAL, end
    #if detection window ends past TOTAL, shrink window and check again


    
    #create 3d model of the map, pulse size, detect size, normal size as the axis
    return 0

def simulate(time, example):
    return qe.dev_sim()

#   Build a normal map off all examples
def build_dataset():
    return 0

def build_data_model():
    #
    return 0


# This section is used to build an array of the data, should be called very rarely, helpful for understanding what the user is looking at
def get_solution(example):
    return qe.dev_data(example)

def get_solutions():
    data = []
    for i in 1000:
        data.append(get_solution(i))
    return data


##################################################
######## PHASE TWO - LOGIC REFINEMENT ############
##################################################
# Teams will now try to dynamically adjust the radar as it scans the target based off their understanding of phase one, and produce a solution to be compared

# import their system for trying to do that
logic = lg.Logic_Machine()

#Take a normalised return and judge the next logical move from it
def interpret_normal_signal(config, signal):
    logic.think(config, signal)

#take a target example and create a normalised map of the results

def compare_solution():
    return 0

