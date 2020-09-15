#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:07:04 2019

@author: Michele Svanera

University of Glasgow.

Code to analyse the csv output results.
 
"""

################################################################################################################
## Imports 

from __future__ import absolute_import, division, print_function


import glob, os
import pandas as pd
# import numpy as np


Path_in = '../in/'
Path_out = '../out/'
Brain_areas = ['EVC', 'HVC', 'MCX', 'CER', 'HIP', 'EAC', 'BST', 'BGA']


##############################################################################
## Functions

def findAorBinFullpath(full_path):
    
    image_name = os.path.basename(full_path)
    image_a_or_b = image_name.split('_')[2]

    return image_a_or_b


def findBrainArea(full_path):
    
    image_name = os.path.basename(full_path)
    area_name = image_name.split('_')[1]

    return area_name



################################################################################################################
## Main

# Read every participants file
all_csv = sorted(glob.glob(Path_in+'*.csv'))

results_df = pd.DataFrame() 

# Sort every partecipants response 
for c_csv_filename in all_csv:
    
    print('\n\n')
    print(c_csv_filename)
    
    # Load csv 
    c_csv_file = pd.read_csv(c_csv_filename)
    c_csv_file = c_csv_file[c_csv_file['question'].notna()]            # Remove lines with nan in question
    
    assert len(c_csv_file) == 72
    
    # Find choices
    choices_made = c_csv_file['choise_selection.clicked_name']
    rows_to_remove = [1 if not (type(c) == str) else 0 for c in choices_made]
    choices_made = [c[7:] if type(c) == str else 'S' for c in choices_made ]
    
    # Find two options
    L_options = c_csv_file['segm_L_slideN']
#    L_options = [area for i,area in zip(rows_to_remove,L_options) if i==0]
    L_options = [findAorBinFullpath(c) if type(c) == str else 'S' for c in L_options]

    R_options = c_csv_file['segm_R_slideN']
#    R_options = [area for i,area in zip(rows_to_remove,R_options) if i==0]
    R_options = [findAorBinFullpath(c) if type(c) == str else 'S' for c in R_options]
    
    # Find which areas corresponds
    areas_questioned = c_csv_file['T1_slideN']
#    areas_questioned = [area for i,area in zip(rows_to_remove,areas_questioned) if i==0]
    areas_questioned = [findBrainArea(c) if type(c) == str else 'S' for c in areas_questioned]

    assert(len(choices_made) == len(L_options) and 
           len(R_options) == len(L_options) and 
           len(R_options) == len(areas_questioned) and 
#           len(rows_to_remove) == (len(areas_questioned) + np.sum(rows_to_remove)) and 
           len(R_options) > 0 and L_options != R_options)

    # Collect selection
    which_is_the_best = []
    for i_choice in range(len(choices_made)):
        
        if choices_made[i_choice] == 'L':
            which_is_the_best.append(L_options[i_choice])
        elif choices_made[i_choice] == 'R':
            which_is_the_best.append(R_options[i_choice])
        elif choices_made[i_choice] == 'S':
            which_is_the_best.append('S')
        else:
            raise Exception('Error: 1.0!')
    


    # Summarise results
    results = {}
    results['name'] = [os.path.basename(c_csv_filename)[:-4]] * len(c_csv_file)
    results['area'] = areas_questioned
    results['L'] = L_options
    results['R'] = R_options
    results['choice'] = which_is_the_best
    results['self_mark'] = list(c_csv_file['rate your expertise (1-10)'])
    results['position'] = list(c_csv_file['your position'])

    # Compile pandas 
    df = pd.DataFrame(results)
    results_df = pd.concat([df, results_df],  axis=0)
    
    print('Cerebrum segm chosen:   %.2f/100 times.' % (100 * which_is_the_best.count('cerebrum') / len(rows_to_remove)))
    print('GT segm chosen:         %.2f/100 times.' % (100 * which_is_the_best.count('GT') / len(rows_to_remove)))
    print('Manual segm chosen:     %.2f/100 times.' % (100 * which_is_the_best.count('manual') / len(rows_to_remove)))
    print('Skipped:                %.2f/100 times.' % (100 * which_is_the_best.count('S') / len(rows_to_remove)))


results_df.to_csv(os.path.join(Path_out,'out.csv'), index=False)









