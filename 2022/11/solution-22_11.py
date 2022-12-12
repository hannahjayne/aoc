import math 
FILE = "input-22_11"


#MONKEY CLASS. OO OO AHRGH AHRGH.
class Monkey:
    
    all_monkeys = []
    relief_level, modulo, do_modulo = 3, 1, True
    operators = {"+": lambda x, y: x + y,"*": lambda x, y: x * y} #used in operation 
    
    #THE MONKEY CONSTRUCTOR.....
    def __init__(self, number, items, operation, test, if_true, if_false):
        self.number = number
        self.operation = operation
        self.test = test
        self.if_true, self.if_false = if_true, if_false
        self.items = items
        
        #keep track of the monkeys & their inspection counts and getting modulo
        self.inspection_count = 0 
        Monkey.modulo = Monkey.modulo * test
        Monkey.all_monkeys.append(self)
        
    #Parses the operation string, using operate dictionary above 
    def operate(self, item):
        op_components = self.operation.split() 
        
        x = int(op_components[0]) if op_components[0] != "old" else item 
        y = int(op_components[2]) if op_components[2] != "old" else item
        
        return Monkey.operators[op_components[1]](x,y) 

    #Have the monkey inspect item, and throw it 
    def inspect_item(self):
        
        while len(self.items) > 0: 
            self.inspection_count += 1 #monkey is inspecting
            
            inspecting = self.items.pop(0)  
            inspecting = math.floor(self.operate(inspecting)/self.relief_level)
            
            if Monkey.do_modulo: inspecting = inspecting % Monkey.modulo
             
            #test is always "if divisible" so we just use modulo 
            if inspecting % self.test == 0: Monkey.all_monkeys[self.if_true].items.append(inspecting)
            else: Monkey.all_monkeys[self.if_false].items.append(inspecting)
            
              
    #Monkeys are identified by their number; this is for my waning sanity
    def __repr__(self): return f"Monkey {self.number}"
 
    
# Makes monkeys, using monkey class, for each monkey in file..
def make_monkeys(file_name):
    file = open(file_name, "r")
    file_lines = file.readlines()
    file.close()
    
    #All this monkey business is 7 lines long, including space between 
    for line in range(0, int((len(file_lines)+1)/7)):
        monkey_info  = file_lines[7*line: 7*line+7]
        
        number = int(monkey_info[0][-3]) 
        items = [int(item.strip(",")) for item in monkey_info[1].split()[2:]]
        operation = (monkey_info[2].split(":")[1]).split("=")[1][1:-1] #keep as string for now
        test = int(monkey_info[3].split()[-1])
        if_true, if_false = int(monkey_info[4].split()[-1]), int(monkey_info[5].split()[-1])
        
        Monkey(number, items, operation, test, if_true, if_false)
         
#TASK ONE: Gets naughtiness score after so many rounds, with relief level 
def get_naughtiness(rounds = 20, relief_level =3): 

    Monkey.relief_level = relief_level    
    
    #I didn't test the actual limit here but it doesn't work with numbers that are too small, strangely enough
    if rounds <= 20: Monkey.do_modulo = False 

    for round in range(0,rounds):
        for monkey in Monkey.all_monkeys: monkey.inspect_item()
        
    inspection_counts = sorted([monkey.inspection_count for monkey in Monkey.all_monkeys])
    naughtiness_score = inspection_counts[-1] * inspection_counts[-2] 

    return naughtiness_score

def main(file_name=FILE):
    make_monkeys(file_name)
    print("Naughtiness Level:",get_naughtiness(10000, 1))
    
main()
 
 