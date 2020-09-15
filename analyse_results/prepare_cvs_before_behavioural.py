#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:02:40 2019

@author: Michele Svanera

University of Glasgow.

Code to create the csv to give as input at the behavioural.

"""

################################################################################################################
## Imports 

from __future__ import division, print_function

import os
import fnmatch
import csv
import numpy as np
import itertools


################################################################################################################
## Paths and Constants

Testing_volumes = ['subj_01', 'subj_02', 'subj_03']

Path_in = '/path/in/'
Path_out = '/path/out/'
Csv_name = 'image_paths.csv'

Areas = ['01_EVC', '02_HVC', '03_MCX', '04_CER', '05_HIP', '06_EAC', '07_BST', '08_BGA']
Questions = ['Please focus on inner (with WM) on outer GM boundaries', 
             'Please focus on inner (with WM) on outer GM boundaries', 
             'Please focus on inner (with WM) on outer GM boundaries', 
             'Please focus on cerebellum', 
             'Please focus on inner (with WM) on outer GM boundaries', 
             'Please focus on inner (with WM) on outer GM boundaries', 
             'Please focus on brainstem and ventricles', 
             'Please focus on basal ganglia and WM and ventricles']
First_line = ['question', 
              'T1_slideN_m_2', 'T1_slideN_m_1', 'T1_slideN', 'T1_slideN_p_1', 'T1_slideN_p_2', 
              'segm_L_slideN_m_2', 'segm_L_slideN_m_1', 'segm_L_slideN', 'segm_L_slideN_p_1', 'segm_L_slideN_p_2', 
              'segm_R_slideN_m_2', 'segm_R_slideN_m_1', 'segm_R_slideN', 'segm_R_slideN_p_1', 'segm_R_slideN_p_2']



################################################################################################################
## Functions

# Compose path with Incipit and the a full path
def composePath(i,initial=''):
    keep_from_path = i.split('/')[-5:]
    keep_from_path = '/'.join(keep_from_path)
    keep_from_path = initial + keep_from_path
    return keep_from_path


def findListOfAnatomical(path_in, identifier='nii.gz'):

    all_anat = []
    for root, _, files in os.walk(path_in):
        for i_file in files:
            if i_file.endswith(identifier):
                all_anat.append(root + '/' + i_file)
    
    return sorted(all_anat)


################################################################################################################
## Main

# Find all png files
files_found = findListOfAnatomical(Path_in, identifier='png')

# Search all anat and segmentation images for: 'anat', 'cer', 'GT', 'manual'
files_found_anat = [i for i in files_found if 'anat' in i]

n_subjects = int(len(files_found_anat)/8/5)

print(str(len(files_found_anat))+" images found!")
print("(means: "+str(n_subjects)+" subjs found)")

assert(len(files_found_anat) > 0)


# Create csv
with open(Path_out+Csv_name, 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(First_line)

    for i_indx, i_subject in enumerate(Testing_volumes):
        
        # Find files for that subject
        i_files_found_anat = [i for i in files_found_anat if i_subject in i]

        for j_indx, j_area in enumerate(Areas):
            
            # Find files for that area
            i_j_files_found_anat = [composePath(i) for i in i_files_found_anat if j_area in i]

            # Reoder the array if not in order
            findSliceNumber = lambda x : int(os.path.basename(x).split('_')[-1][:-4])      # ex. '64'
            slice_numbers = [findSliceNumber(i) for i in i_j_files_found_anat]
            i_j_files_found_anat = [i_j_files_found_anat[i] for i in np.argsort(slice_numbers)]



            # At this point, we have 3 segmentations: cer, GT, and man.
            # We need to create 3 rows (since we do 3 comparisons) 
            # e randomly select the order between the two first
            comb_pairs = itertools.combinations(['cerebrum', 'GT', 'manual'], 2)

            for r_comb in comb_pairs:       # ex. ('GT', 'manual'): GT vs manual
                
                # Compose the row of the csv file
                q_row = []
                q_row.append(Questions[j_indx])

                for f_file in i_j_files_found_anat:
                    q_row.append(f_file)
                    
                rdm_selection = np.random.permutation(r_comb)
                for s_segm in rdm_selection:
    
                    for m_file in i_j_files_found_anat:
                        convertValue = lambda x, y : x.replace('_anat_','_'+y+'_')
                        q_row.append(convertValue(m_file, s_segm))
            
                # Write line
                assert(len(First_line) == len(q_row) and len(q_row) > 0)
                filewriter.writerow(q_row)
            

print("\n**** Done! ****\n")












    
