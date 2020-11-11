# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:02:39 2020

@author: chris

Markov Chain Monte Carlo
"""

from random import *

'''
random_variables(): Creates a list of 5 variables that are randomly set to True
or False.
Return type: list(bool)
    list of randomly assigned variables.
'''
def random_variables():
    var_list = []
    for x in range(0,5):
        rand = randint(0,100)
        print(rand)
        if rand > 50:
            var_list.append(True)
        else:
            var_list.append(False)
            
    return var_list

def markov_chain(curr_state, prob_matrix):
    next_state = []
    
    # To calculate next state, multiply the curr_state by prob_matrix
    
    
    return next_state

