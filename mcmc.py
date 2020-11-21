# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:02:39 2020

@author: chris

Markov Chain Monte Carlo
"""

from random import *

NUM_RUN = 5
NUM_INSTANCES = 10000

COVID = 0
FEVER = 1
COUGH = 2
FEVER_COUGH = 3
COUGH_NAS = 4
NAS = 5
NAS_FEVER = 6

PROBS = []



def random_variables():
    # Make empty list
    var_list = []
    # Randomly assign true or false for each symptom, allows for weighted
    # random numbers
    for x in range(0,6):
        rand = randint(0,100)
        if rand > 50:
            var_list.append(True)
        else:
            var_list.append(False)
        var_list.append(True)
                  
    return var_list

'''
This next function is a long, hot mess. I'm sorry.
'''
def calculate_prob(var_list):
    curr_prob = 1
    # Checking if covid is true or not, then finding probability for state 1 
    # conditions
    if var_list[COVID]:
        curr_prob = curr_prob * 0.01
        # Fever
        if var_list[FEVER]:
            curr_prob = curr_prob * 0.78
        else:
            curr_prob = curr_prob * 0.22
        # Cough
        if var_list[COUGH]:
            curr_prob = curr_prob * 0.98
        else:
            curr_prob = curr_prob * 0.02
        # Nausea
        if var_list[NAS]:
            curr_prob = curr_prob * 0.59
        else:
            curr_prob = curr_prob * 0.41
    else:
        # Fever
        if var_list[FEVER]:
            curr_prob = curr_prob * 0.1
        else:
            curr_prob = curr_prob * 0.9
        # Cough
        if var_list[COUGH]:
            curr_prob = curr_prob * 0.1
        else:
            curr_prob = curr_prob * 0.9
            # Nausea
        if var_list[NAS]:
            curr_prob = curr_prob * 0.2
        else:
            curr_prob = curr_prob * 0.8
            
    # Checking second tier symptoms
    if var_list[COUGH]:
        if var_list[FEVER]:
            if var_list[FEVER_COUGH]:
                curr_prob = curr_prob * 0.8
            else: 
                curr_prob = curr_prob * 0.2
        else:
            if var_list[FEVER_COUGH]:
                curr_prob = curr_prob * 0.3
            else: 
                curr_prob = curr_prob * 0.7
        if var_list[NAS]:
            if var_list[COUGH_NAS]:
                curr_prob = curr_prob * 0.76
            else: 
                curr_prob = curr_prob * 0.24
        else:
            if var_list[COUGH_NAS]:
                curr_prob = curr_prob * 0.42
            else: 
                curr_prob = curr_prob * 0.58
    else:
        if var_list[FEVER]:
            if var_list[FEVER_COUGH]:
                curr_prob = curr_prob * 0.95
            else: 
                curr_prob = curr_prob * 0.05
        else:
            if var_list[FEVER_COUGH]:
                curr_prob = curr_prob * 0.2
            else: 
                curr_prob = curr_prob * 0.8
        if var_list[NAS]:
            if var_list[COUGH_NAS]:
                curr_prob = curr_prob * 0.29
            else: 
                curr_prob = curr_prob * 0.71
        else:
            if var_list[COUGH_NAS]:
                curr_prob = curr_prob * 0.05
            else: 
                curr_prob = curr_prob * 0.95
    # Checking fever and nausea           
    if var_list[FEVER]:
        if var_list[NAS]:
            if var_list[NAS_FEVER]:
                curr_prob = curr_prob * 0.85
            else: 
                curr_prob = curr_prob * 0.15
        else:
            if var_list[NAS_FEVER]:
                curr_prob = curr_prob * 0.63
            else: 
                curr_prob = curr_prob * 0.37
    else:
        if var_list[NAS]:
            if var_list[NAS_FEVER]:
                curr_prob = curr_prob * 0.58
            else: 
                curr_prob = curr_prob * 0.42
        else:
            if var_list[NAS_FEVER]:
                curr_prob = curr_prob * 0.08
            else: 
                curr_prob = curr_prob * 0.92
        
            
    return curr_prob

def flip_given_bit(given_var_list, bit):
    # Make empty list to store conditional probability
    
    # Make copy of given list of vars
    new_var_list = given_var_list.copy()
    
    # Flip the given bit
    if new_var_list[bit]:
        new_var_list[bit] = False
    else:
        new_var_list[bit] = True
    return new_var_list

def calc_conditional_prob(var_list, bit):
    # Calculate probabilty of current assignment
    curr_prob = calculate_prob(var_list)
    # Calculate conditional probability for each node

    # Flip the bit and find new probability
    conditional_list = flip_given_bit(var_list, bit)
    new_prob = calculate_prob(conditional_list)

        
    # Calculate the conditional probability
    conditional_prob = curr_prob / (curr_prob + new_prob)
    return conditional_prob

def choose_bit():
    num = randint(0,471)
    if num == 471:
        bit = COVID
    elif num < 470 and num >= 372:
        bit = COUGH
    elif num >= 294:
        bit = FEVER
    elif num >= 235:
        bit = NAS
    elif num >= 155:
        bit = FEVER_COUGH
    elif num >= 70:
        bit = NAS_FEVER
    else:
        bit = COUGH_NAS
        
    return bit

def main():
    covid_counter = 0
    for run_num in range(0,NUM_RUN + 1):
        my_list = random_variables()
        for instance_num in range(0, NUM_INSTANCES + 1):
            curr_bit =  choose_bit()
            if my_list[0]:
                covid_counter += 1
            prob = calc_conditional_prob(my_list, curr_bit)
            PROBS.append(prob)
            if instance_num > 0 and instance_num % 1000 == 0:
                print("Run number: ", instance_num)
                print("Covid percent: ", covid_counter/instance_num)
                print()
    
    
    
main()
