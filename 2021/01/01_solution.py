FILE = "input"


def do_task(task, file_name = FILE,):
    file = open(file_name,"r")
    answer = task(file)
    file.close()
    return answer
    
#task one
def task_one(file):
    counter, previous = -1, 0
    
    for line in file: 
        counter += 1 if int(line[:-1]) > previous else 0
        previous = int(line[:-1])
    
    return counter        

#alternate method for task one - why would you do it this way, silly!!!
def task_one_alt(file):
    lines = file.readlines()
    lines = list(zip(lines, lines[1:]+lines[:1]))[:-1]
    return sum([True for each in lines if int(each[0]) < int(each[1])])
    
def task_two(file, n=3):
    lines = file.readlines()
    counter, previous = -1, 0
    for i in range (0, len(lines)):
        window = [int(x[:-1]) for x in lines[i:i+n]]
        counter += 1 if sum(window) > previous else 0 
        previous = sum(window)
    
    return counter

         
def print_solutions():
    print("Task one:", do_task(task_one))
    print("Task two:", do_task(task_two))
    
     
print_solutions()
 