FILE = "input-22_10"
import numpy as np

NOOP_LEN = 1
ADDX_LEN = 2

STRENGTH_CYCLES = [20, 60, 100, 140, 180, 220]

DIMENSIONS = (6,40)

def do_tasks(task, file_name = FILE):
    actions = get_actions(file_name)
    print(task(actions))
    return 


#Get's actions as dictionary, wherein key is the cycle the action is executed and value is action done to x
def get_actions(file_name =FILE):
    
    file = open(file_name, "r")
    
    current_cycle, actions = 0, {}
    
    for each in file:
        if each[0:4] == "addx": #so if we have to add x...
            value = int(each.split()[1])
            actions[current_cycle + ADDX_LEN] = value  #executes on current cycle + length of time for addx
            current_cycle += 2 
            
        else: current_cycle +=1 #otherwise it's noop! we just keep on truckin' 
        
    file.close()
    return actions
   

#Gets sum of signal strengths at specific cycles 
def task_one(actions, strength_cycles = STRENGTH_CYCLES):
    
    x_reg, strength_sum = 1, 1 
  
    
    #actions dict's keys are the cycles when x_reg is manipulated; get these
    execution_times, strength_cycles = sorted(actions.keys()), sorted(strength_cycles)
    
    #go through all the actions, and perform them
    for cycle in execution_times:
        
        if len(strength_cycles) == 0: break  #also if no more strength cycles => stop, we dont need more 
        if cycle > strength_cycles[0]: 
            strength_sum += strength_cycles.pop(0) * x_reg  
       
        x_reg += actions.pop(cycle)  #important that we manipulate x_reg after, as we may have passed a strength_cycle 
    
    return strength_sum
            
#Draws CRT to new file, using instructions       
def task_two(actions):
    
    crt_drawing = np.full(DIMENSIONS,".",dtype=str) #all . by default
    x_pos = 1
    
    execution_times = sorted(actions.keys())
    
    for cycle in range(0, DIMENSIONS[0] * DIMENSIONS[1]):
        
        if cycle in execution_times:  #sprite is moved 
            x_pos += actions.pop(cycle)
    
        at_pixel = cycle % DIMENSIONS[1] #looking at this pixel 
        row_index = int(np.floor(cycle / DIMENSIONS[1])) #on this specific row
        
        if at_pixel in range(x_pos-1, x_pos+2): #if pixel is on sprite position then set to #
            crt_drawing[row_index][at_pixel] =  "#"

    #saving to .txt file; read the output from there 
    np.savetxt("crt_drawing.txt", crt_drawing, delimiter="", fmt="%s")
    
    return "Saved to file crt_drawing.txt"
     
 
 

 