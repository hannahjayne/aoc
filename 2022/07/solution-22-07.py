FILE = "input-22_07"

LIMIT = 100000
TOTAL, NEED = 70000000, 30000000

#DIRECTORY CLASS 
class Dir(): 
    
    def __init__(self, dir_name):
        self.dir_name= dir_name
        self.dirs, self.files = [], []
        self.size = 0 

    def add_dir(self, directory): self.dirs.append(directory)
    def add_file(self, file): self.files.append(file)
    
    def get_by_name(self, name):
        for directory in self.dirs:
            if directory.dir_name == name: return directory  
          
    def calculate_size(self):
        in_file = sum([file for file in self.files])
        for directory in self.dirs: in_file += directory.calculate_size()
        self.size = int(in_file) 
        return in_file 
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.dir_name})"
    

#Builds file directory, going through instructions in the file; returns root 
def build_file_dir(file):

    pwd = [Dir("/")] #keeps track of current directory path
     
    for instruction in file: 

        ##CHANGE CURRENT DIRECTORY 
        if instruction[0:4] == "$ cd": 
            if instruction[5] == ".": pwd.pop() #go back a dir
            elif instruction[5] == "/": pwd = pwd[:1] #go to root
            else: pwd.append(pwd[-1].get_by_name(instruction[5:-1])) #put dir on end of pwd
            
        ##ADDING LS CONTENTS
        elif instruction[0] != "$": 
            contents = instruction.split() 
            if contents[0] == "dir": pwd[-1].add_dir(Dir(contents[1])) #Mmakes dir in current directory
            else: pwd[-1].add_file(int(contents[0])) #adds files to current directory
    
    #Deduce the size of all directories, starting from the root 
    pwd[0].calculate_size()
    
    return pwd[0] 

#TASK ONE: Similar logic to Dir.calculate_sizem which already deduced size of all directories
def task_one(root):
    total_sum = 0 
    
    for directory in root.dirs:
        total_sum += directory.size  if directory.size <= LIMIT else 0
    
        #if a directory contains directories => call function on itself to get sum of those      
        if len(directory.dirs) != 0: total_sum += task_one(directory) 
        
    return total_sum

#TASK TWO: Similar logic again; go through from root using deduced sizes
#... Probably could have been done simultaneously with task 1 - but wanted them separate!!
def task_two(root): 
    to_delete = NEED - (TOTAL - root.size) #where free space = total space - root.size
    return get_sizes(root, to_delete).pop()
 
def get_sizes(root, to_delete):
    sizes = [] #get all sizes... 
    
    for directory in root.dirs:
        if directory.size >= to_delete: sizes.append(directory.size)
        if len(directory.dirs) != 0: sizes += get_sizes(directory, to_delete)
    return min([sizes]) #we'll always be seeking minimum, so it's fine if we only get that from inner dirs


def print_tasks(file_name = FILE):
    file = open(file_name, "r")
    root = build_file_dir(file)
    file.close()
    
    print("TASK ONE:", task_one(root))
    print("TASK TWO:", task_two(root))
    return

print_tasks()