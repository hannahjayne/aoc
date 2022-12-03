FILE = "input"

"""
Gets the priority score for individual items with ord(); A-Z need to score between 27-52; a-z need to score between 1-26.
"""
def priority_score(item):
    return ord(item) - 38 if item.isupper() else ord(item) - 96

"""
Deduces the mutual item (character) across list of strings. Returns the score of that item, using priority_score.
"""
def mutual_item_score(n_rucksacks):
    mutual_item = set.intersection(*map(set, n_rucksacks)) # Change list to sets, then just use intersection to get mutual item
    return priority_score(mutual_item.pop()) #Only one item in mutual_item set - so we just pop it off!



### TASK ONE ###

"""
Sums up the priorities of each rucksack, depending on scoring function. Returns this sum
"""
def task_one(file_name):

    file = open(file_name, "r")
    priority_sum = 0

    for line in file: priority_sum += mutual_item_score(get_compartments(line[:-1])) # knock off that blasted new line character...
        
    file.close()
    return priority_sum

"""
Gets the two compartments of a single rucksack by slicing it. Returns these compartments as list
"""
def get_compartments(rucksack):
    compartment1, compartment2 = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]
    return [compartment1, compartment2]



### TASK TWO ###

"""
Deduces the mutual item (i.e: badge) across n rucksacks. Then sums up the priority of those badges and returns this score
"""
def task_two(file_name, n=3):

    file = open(file_name, "r")
    lines = file.readlines()

    priority_sum = 0

    for i in range(0, len(lines), n):
        n_rucksacks = lines[i:i+n]
        n_rucksacks = [rucksack[:-1] for rucksack in n_rucksacks] #There's definitely a faster way of doing this... 

        priority_sum += mutual_item_score(n_rucksacks)

    file.close()

    return priority_sum



### PRINT SOLUTIONS ###

def solutions():
    print("SOLUTION 1:", task_one(FILE))
    print("SOLUTION 2:", task_two(FILE))


solutions()
