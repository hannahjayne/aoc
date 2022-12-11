import numpy as np

FILE = "input"
DAYS = 80

resets_to = 6
born_at = 8


def do_task(task, file_name = FILE):
    
    file = open(file_name,"r")
    fish = get_numbers(file)
    file.close()
    
    return task(fish)
    

def get_numbers(file):
    for line in file: return np.array(list(map(int,line.split(","))))
     

#TASK ONE: this is horrible. dont do this.
"""
def task_one(fish, days = DAYS):
    
    for i in range(0,DAYS): 
        fish[fish == 0] = resets_to + 1
        fish = fish - 1 
        new_fish = np.full((np.count_nonzero(fish == resets_to)), born_at) 
        fish = np.concatenate((fish, new_fish)) 
       
    return len(fish)
"""

def task_one(fish, days = DAYS):
    counts = np.bincount(fish)
    
    test, new_fish = 6, 0
    for i in range(0,DAYS):
        if test == 0: test, new_fish = 6, new_fish + 1
        test -= 1 
    print(new_fish)
        
    return
    

## PRINT SOLUTIONS ###
def print_solutions():
    print("TASK ONE:",do_task(task_one))
    #print("TASK TWO:",do_task(task_two))
    return

print_solutions() 