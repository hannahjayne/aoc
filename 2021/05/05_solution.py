# -*- coding: utf-8 -*-
 
import numpy as np

FILE = "input"
 

#ORIGINALLY: diagram was going to resize whenever it encountered a number bigger than itself - however this didnt work
#Unhappy with cheating it to be this size. I'll try to fix it another time.
DIAGRAM_SIZE = (1000,1000)

#Opens file; iterates through, and gets line segments; computes, depending on which task is called
def do_task(task,file_name = FILE):    
    file = open(file_name, "r")
    diagram = np.zeros(shape=DIAGRAM_SIZE, dtype = int) #
    
    for line in file:
        
        segments = line[:-1].split(" -> ") 
        segments = [list(map(int, x.split(","))) for x in segments] #gets list of co-ords 

        #renaming them, for the sake of readability
        y1, y2, x1, x2 = segments[0][0], segments[1][0], segments[0][1], segments[1][1] 
        task(x1,x2,y1,y2, diagram) #task function will "draw" lines on diagram depending on task criteria
    
    file.close()
    return (diagram>1).sum() #returns intersections - i.e, elements > 1
         
#TASK ONE: increments horizontal and vertical lines only
def task_one(x1, x2, y1, y2, diagram):
    
    #pretty straightforward. we just slice numpy array to get section of col/row respectively
    if x1 == x2: diagram[x1, min(y1,y2):max(y1+1,y2+1)] += 1
    elif y1 == y2: diagram[min(x1, x2):max(x1+1, x2+1),y1] += 1 
    
    return diagram

#TASK TWO: incremenets all lines, including diagonals
def task_two(x1, x2, y1, y2, diagram):
    
    #same as task_one()... 
    if x1 == x2: diagram[x1, min(y1,y2):max(y1+1,y2+1)] += 1
    elif y1 == y2: diagram[min(x1, x2):max(x1+1, x2+1),y1] += 1 
    
    #for diagonals: check direction by comparing x1,x2 and y1,y2; set to neg if going in neg direction
    else:
        x, y = 1, 1  
        if not bool(x2-x1 >0): x = -1 
        if not bool(y2-y1 > 0): y = -1 
            
        #and then use for loop, and increment each cell on diagonal 
        for i in range(0, abs(x1-x2)+1): diagram[x1+(x*i), y1+(y*i)] += 1
    
    return diagram
    
     
 
## PRINTING ##
def print_solutions():
    print("TASK 1:", do_task(task_one))
    print("TASK 2:", do_task(task_two))
    return
        
print_solutions()
