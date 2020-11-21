# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:02:39 2020

@author: chris

Markov Chain Monte Carlo
"""

from random import *

COVID = 0
FEVER = 1
COUGH = 2
FEVER_COUGH = 3
COUGH_NAS = 4
NAS = 5
NAS_FEVER = 6

CBT = []



def random_variables():
    # Make empty list
    var_list = []
    # Randomly assign true or false for each symptom, allows for weighted
    # random numbers
    for x in range(0,7):
        rand = randint(0,100)
        if rand > 50:
            var_list.append(True)
        else:
            var_list.append(False)
                  
    return var_list

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
            
    # Checking second tier symptoms
    if var_list[FEVER]:
        
            
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

def calc_conditional_prob(var_list):
    # Calculate probabilty of current assignment
    curr_prob = calculate_prob(var_list)
    print("Original prob: ", curr_prob)
    # Calculate conditional probability for each node
    for bit in range(0,7):
        # Flip the bit and find new probability
        conditional_list = flip_given_bit(var_list, bit)
        new_prob = calculate_prob(conditional_list)
        print("Curr assignment: ", var_list)
        print("New assignment: ", conditional_list)
        print("New prob: ", new_prob)
        
        # Calculate the conditional probability
        conditional_prob = curr_prob / (curr_prob + new_prob)
        CBT.append(conditional_prob)
        new_prob = 0

def main():
    my_list = random_variables()
    
    calc_conditional_prob(my_list)
    print(CBT)
    
    
    
main()
