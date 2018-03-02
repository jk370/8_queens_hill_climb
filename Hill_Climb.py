# Code to compute local maximum from starting state
import numpy as np
from copy import deepcopy

class Problem:
    def __init__(self):
        '''Creates initial node'''
        self.node = Node()
        
    def get_node(self):
        '''Returns initial node'''
        return self.node
        
class Node:
    def __init__(self, rows = 8, columns = 8):
        '''Sets up initial state of node (all Queens on row 1)'''
        self.rows = rows
        self.columns = columns
        self.state = [0]*columns
        
    def get_state(self):
        '''Returns current state of the node'''
        return self.state
    
    def set_state(self, board):
        '''Sets current state to board array passed in'''
        self.state = board
    
    def get_highest_neighbour(self):
        '''Finds highest neighbour from current state of the node'''
        queens = self.columns
        initial_position = self.state
        max_score = self.compute_value()
        best_neighbour = self
        
        # Loop through each queen (column)
        for i in range(0, queens):
            # Loop through each row
            for j in range(0, queens):
                # Reset test position - deep copy due to prevent shared object
                test_position = deepcopy(initial_position)
                
                # Ignore current queen position
                if test_position[i] != j:
                    # Create new node for queen movement
                    test_position[i] = j
                    nb = Node()
                    nb.set_state(test_position)
                    #print("Queen:", i, "Row:", j, "Test:", test_position)
                    # Test neighbour node and keep if scores better
                    if nb.compute_value() < max_score:
                        max_score = nb.compute_value()
                        best_neighbour = deepcopy(nb)
                        
        return best_neighbour
    
    def compute_value(self):
        '''Computes value of current board state'''
        positions = self.state
        queens = self.columns
        score = 0
        # Loop through the queen on each column
        for i in range(0, queens):
            # Look ahead to prevent double counting
            for j in range(i+1, queens):
                hor_diff = j-i
                ver_diff = abs(positions[j] - positions[i])
                # Add to score if attack is found
                if positions[j] == positions[i] or hor_diff == ver_diff:
                    score += 1
        return score
    
def hill_climb(problem):
    '''Computes the local maximum of the problem using hill_climb'''
    current = problem.get_node()
    # Loop until local maximum found
    while(True):
        neighbour = current.get_highest_neighbour()
        if neighbour.compute_value() >= current.compute_value():
            return current
        current = neighbour
    
s = Problem()
local_max = hill_climb(s)
print("Local maximum is:", local_max.get_state())
print("Number of hits: %d" % local_max.compute_value())