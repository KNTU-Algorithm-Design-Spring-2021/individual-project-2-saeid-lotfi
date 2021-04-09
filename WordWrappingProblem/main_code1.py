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
    #printing the words based on break points
    
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


#this function print the given sentence to a well shaped paragraph
def word_wrapper(sentence, M):
    #iputs
    #sentence: a string of characters
    #M: maximum width of paragraph
    #output
    #print the sentence in a good shape
    
    #word extraction
    #list of individual words
        #first element is blank to start from index one
    word_list = [''] + sentence.split(' ')
    #list of words length
        #first element is zero to start from index one
    word_lentgh_list = np.array([len(word) for word in word_list])
    #number of all words
    n = len(word_lentgh_list) - 1
    
    #making cost matrix
        #first column and row are extra to start from index [1, 1]
    line_cost_matrix = np.ones([1 + n, 1 + n])
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            #getting cost of putting i'th word to j'th word in one line
            line_cost_matrix[i, j] = line_cost_cal(word_lentgh_list, i, j, M)
    
    #making total cost array with dynamic prgramming
    #first element is zero
    C = [0]
    #keeping break points for print phase
    break_points = [0]
    #getting C[i] from C[i-1]
    for i in range(1, n + 1):
        #possible ways of breaking the words for last line with use of up-to i'th word
        candid_list = [(C[mid_index - 1] + line_cost_matrix[mid_index, i]) for mid_index in range(1, i + 1)]
        #selecting minimum for best solution up-to i'th word
        C.append(min(candid_list))
        #keeping the solution index as break index
        break_points.append(candid_list.index(min(candid_list)) + 1)
        
    
    #showing result
    #printing paragraph width with stars
    print('*' * M)
    #calling "seq_printer" to show the result
    seq_printer(word_list, break_points)
    #printing paragraph width with stars
    print('*' * M)
    

#performing on a sequence with dynamic programming method




#showing result
