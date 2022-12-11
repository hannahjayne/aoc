FILE = "input"

# CONSTANTS#
LETTER_DIST = 4 #letter_distance is used for reading file; it's the distance between crate labels
N, A, B = 1, 3, 5 #N is number of crates moved; A is source stack; B is destination stack

### SET UP ### 

#Gets the initial stacks of crates as a dictionary. Keys are stack numbers; values are lists of stacks
def get_initial_stacks(lines):
    
    for line in lines: #We find the end of lines of crates by getting "label row" 
        if line[1] == "1": break 
            
    rows = lines[0:lines.index(line)] #so take slice of file lines to get stacks
    rows.reverse() 
     
    stack_count = int(lines[lines.index(line)][-3]) #final stack label is at -3 on line
    stacks = dict.fromkeys(range(1, stack_count +1),"") 
    
    for row in rows: #now for every row of crates     
        for i in range(1, len(row), LETTER_DIST): #we iterate through each crate, using letter distance as step
            stack_no = int((i-1)/LETTER_DIST) + 1  #and now we can deduce stack_number with letter distance, as they're aligned
            if row[i] != " ": stacks[stack_no] += row[i] #also - only appends if crate exists!
     
    #there were issues creating values as lists - so im converting from strings -> lists afterwards. might fix later.
    for i in range(1, stack_count+1): stacks[i] = list(stacks[i])
    
    return stacks


#Takes file, establishes stacks&instructions; then iterates through instructions, and performs whatever task function is used to get result
def do_task(task, file_name=FILE):
    
    file = open(FILE, "r")
    lines = file.readlines()
    file.close()
     
    #separate out stacks from instructions
    stacks = get_initial_stacks(lines)
    instructions = lines[len(stacks)+1:]
    
    #then parse instructions & move crates in stacks depending on which task function is called
    for line in instructions:
        get_numbers= line.split(" ")
        n, a, b  = int(get_numbers[N]), int(get_numbers[A]), int(get_numbers[B][:-1])
        stacks = task(n, a , b, stacks)
      
    #result is top crate so we just pop each off the top
    result = [stacks[x].pop() for x in range(1, len(stacks)+1)]
   
    #then return as a string for convenience
    return "".join(result)


### TASK FUNCTIONS ###

#TASK ONE: pop off from stack a n times, and append to stack b each time; then return stacks
def task_one(n, a, b, stacks):
    for i in range(0, n): stacks[b].append(stacks[a].pop()) 
    return stacks
    
#TASK TWO: get slice from stack a, of n length; rewrite stack a, then append moved crates slice to stack b
def task_two(n, a, b, stacks):
    moved_crates = stacks[a][len(stacks[a])-n:]
    stacks[a] = stacks[a][:-n]
    for crate in moved_crates: stacks[b].append(crate)
    return stacks  


## PRINT SOLUTIONS ###
def print_solutions():
    print("TASK ONE:",do_task(task_one))
    print("TASK TWO:",do_task(task_two))
    return

print_solutions()
