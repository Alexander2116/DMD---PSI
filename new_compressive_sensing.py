# -*- coding: utf-8 -*-
# -*- python=3.8.x
"""
Created on 06/07/2023

New version of compressive sensing.
The goal is to create real-time implementation and seq creation.
DMD is supposed to load once and run in a loop so user can create a sequence.

@author: Alex Kedziora
"""

import ajiledriver as aj
from new_dmd_control import DMD
import os
import numpy as np
import pickle


def load_list_images() -> list:
    # Loads file NAMES present in ./patterns
    # All paterns should be created before hand using pattern_generator.py
    patterns = []
    for file in os.listdir("./patterns"):
        # Check whether file is in pickle format or not
        if file.endswith(".pickle"):
            patterns.append(file)
    return patterns

def add_image_to_seq(npImage : np.array, imageID : int) -> None:
    # Add image to the main sequence (currently selected sequence) 
    dmd.add_sub_sequence(npImage, imageID)

def print_list(patterns : list) -> None:
    # Prints all items in the lsit 
    os.system('cls')
    print("The list of patterns available:")
    for i in range(len(patterns)):
        print(str(i) + " : " + patterns[i])

def switch_menu() -> int:
    # Basic menu to create a sequence and to run the project
    # Return 0 if works, -1 if exit (or non-exisiting option is given)
    # switch-case not defined in py3.8, available in py3.10
    imageID = 0
    image = np.array
    print("Options:")
    print("1: Create new main sequence")
    print("2: Create subsequences")
    print("3: Run")
    print("4: Exit")
    option = input("Select option: ")

    # Create new sequence (not needed if only one main sequence is loaded)
    if(option == "1"):
        dmd.create_project()
        dmd.create_main_sequence(5)
        print("The main sequence ID is: " + dmd.main_sequence_ID)
        return 0
    
    # Create subsequence (main option to create a list of patterns to display)
    elif(option == "2"):
        patterns = load_list_images()
        continue_loop = True
        while(continue_loop):
            os.system('cls')
            print(len(patterns))
            inp = input("Add another sequence [y/n]: ")
            if(inp == "y"):
                imageID += 1
                print_list(patterns)
                pattID = int
                pattID = input("Select ID of the patterns to add it to the main sequence: ")
                image = pickle.load(open("./patterns/" + patterns[int(pattID)], 'rb'))
                add_image_to_seq(image,imageID)
            else:
                continue_loop = False
        return 0

    # Run the project (loads the created pattern and runs it)
    elif(option == "3"):
        dmd.stop_projecting()
        # Load the defined project, and wait for completion
        dmd.start_projecting()
        input("Press Enter to stop the sequence")
        dmd.stop_projecting()
        return 0
    
    # Exit
    elif(option == "4"):
        return -1

    # Non-existing option given = exit
    return -1

def main():
    dmd.create_project()
    dmd.create_main_sequence(5)
    print("Project and initial sequence are created")

    option = 0
    continue_loop = True

    while(continue_loop):
        option = switch_menu()
        if(option == -1):
            continue_loop = False
            return



if __name__ == "__main__":
    global dmd
    dmd = DMD()
    main()