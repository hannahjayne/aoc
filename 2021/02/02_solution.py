FILE = "input"

#TASK ONE
def task_one(file):
    
    #where x, y are horizontal and vertical positions
    x, y = 0, 0 

    for line in file:
        if line[0] == "f": x += int(line[-2])
        elif line[0] == "u": y -= int(line[-2]) 
        else: y += int(line[-2]) 
    
    return x*y

#TASK TWO
def task_two(file):
    
    #where a is the aim
    x, y, a = 0, 0, 0
    
    for line in file:
        if line[0] == "f": x, y = x + int(line[-2]), y + int(line[-2]) * a
        elif line[0] == "u": a -= int(line[-2])
        else: a += int(line[-2])
        
    return x * y
    

#PRINTING SOLUTIONS
def do_task(task, file_name = FILE):
    file = open(file_name, "r")
    answer = task(file)
    file.close()
    return answer 

def print_solutions():
    print("TASK 1:", do_task(task_one))
    print("TASK 2:", do_task(task_two))
    
print_solutions()
