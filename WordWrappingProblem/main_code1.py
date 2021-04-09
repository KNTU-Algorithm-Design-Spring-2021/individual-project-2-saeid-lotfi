#importing libraries
import numpy as np


#defining useful functions
#this function calculate the cost if we put words
#from starting index to ending index in one line
def line_cost_cal(word_length_list, start_index, end_index, M):
    #inputs
    #word_length_list: a list containing length of words
        #first element is zero to reserve zero index and start from one
    #start_index: index of starting word
    #end_index: index of ending word
    #M: maximum length of line
    #output
    #cost of putting words from starting index to ending index in one line
    
    #helpful variables
    #n: index of last word
    n = len(word_length_list) - 1
    
    #getting cost
    cost = (M - (end_index - start_index) - np.sum(word_length_list[start_index: end_index + 1]))
    #if cost is negative, we return +infinity cause its impossible
    if cost < 0:
        return 100000
    #if its positive but:
    else:
        #if ending index is last index we return zero cause last line doesnt matter
        if end_index == n:
            return 0
        #if none of those we will return calculated cost
        else:
            return cost


#this function print the words in some lines based on break points
def seq_printer(word_list, break_points):
    #inputs
    #word_list: a list containing all words
        #first element is blank string to reserve zero index and start from one
    #break_points: a list containing break points of sentence
    #output
    #just print the sentence in a good shape
    
    #helpful variables
    start_index = len(break_points)
    
    #keeping each line in elements of list
    lines = []
    while True:
        #starting from last line
        end_index = start_index - 1
        start_index = break_points[end_index]
        lines.append(' '.join(word_list[start_index: end_index + 1]))
        #if we reached the first element its over
        if start_index == 1:
            break
    
    #printing from last line to first line
    for i in range(len(lines)-1, -1, -1):
        print(lines[i])


#performing on a sequence with dynamic programming method




#showing result
