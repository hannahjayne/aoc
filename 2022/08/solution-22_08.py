import numpy as np

FILE = "input-22_08"



#Takes file and builds trees as np array (typed integer)
def as_array(file_name):
    file = open(file_name, "r") 
    as_lines = file.readlines()
    file.close()
    
    return np.array([[no for no in line[:-1]] for line in as_lines], dtype=int)

#Does task, prints solution; pass it the ask function 
def do_task(task,file_name = FILE):
    trees = as_array(file_name) 
    print("solution:", task(trees))



#### TASK 1: FIND NUMBER OF TREES ####

#Takes trees array; returns array of which trees are visible
def get_visible(trees):
    
    is_visible = np.zeros(trees.shape, dtype=bool)
    
    #Goes by each side, by rotating array each time
    for side in range(0,4):
        is_visible[0] = [True for tree in range(0, min(trees.shape))] #sets outermost to be visible
        is_visible = visible_from_side(trees, is_visible) 
        trees, is_visible = np.rot90(trees), np.rot90(is_visible)
        
    return is_visible
    
#Deduces which trees are visible from one side 
def visible_from_side(trees, is_visible):
    rows, cols = trees.shape
    tallest = np.zeros((1,cols), dtype=int) #keeps track of tallest tree in col
    
    for tree_row in range(0, rows):
        
        #Set to true if tree is shorter than 
        is_visible[tree_row] = [True if trees[tree_row][col] > tallest[0][col] else is_visible[tree_row][col] for col in range(0, cols)]
        
        #subtract current row from tallest; if any elements are neg. then there's a new tallest tree for that column
        compare = tallest - trees[tree_row] 
        tallest[0] = [trees[tree_row][height] if compare[0][height] < 0 else tallest[0][height] for height in range (0, cols)]
         
    return is_visible

#TASK 1: Return sum of all visible, from the outside
def task_one(trees):
    is_visible = get_visible(trees) #gets visible 
    return np.sum(is_visible) #sum of all true values
    


#### TASK 2: FIND SCENIC SCORES ####

#Goes through each tree and calculates the scenic scores
def calculate_scenic(trees):
    scenic_scores = np.zeros(trees.shape, dtype=int)
    rows, cols = trees.shape
    
    for row in range(0, rows):
        for col in range(0, cols):
    
            #takes the column for that tree as slice; takes the row for that tree as slice
            tree_row, tree_col = trees[row, 0:], trees[0:, col]
            left, right = score_by_slice(tree_row, col)
            up, down = score_by_slice(tree_col, row)
            scenic_scores[row][col] = left * right * up * down
 
    return scenic_scores

#Calculates the scores along an axis for a tree, when given a slice
def score_by_slice(tree_slice, index): 
    
    #... it occurs to me I dont know my left from right
    left_score, right_score = 0, 0 
    to_left, to_right = tree_slice[index:], tree_slice[:index] #get heights to left and right of tree 
    tree_height = tree_slice[index] #height of current tree
    
    if len(to_left) != 0:
        for height in to_left[1:]: 
            left_score += 1 #increment for each tree to left
            if tree_height <= height: break  #then if we find the one bigger, we break
        
    if len(to_right) != 0:
        for height in to_right[-1::-1]: #note, we move backwards through other list
            right_score += 1 
            if tree_height <= height:  break 
        
    return left_score, right_score
    
#TASK 2: returns the max score from the scenic scores array
def task_two(trees):
    scenic_scores = calculate_scenic(trees)
    return np.max(scenic_scores)

 

 