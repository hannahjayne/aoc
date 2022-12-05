import numpy as np

FILE = "input"
BINGO_N = 5 #size of bingo board
 
### SET UP FOR EACH TASK FUNCTIONS ###
#Note: for this day, task one and two could really be done simultaneously.
def do_task(task, file_name = FILE,):
    
    file = open(file_name,"r")
    lines = file.readlines()
    
    draw_numbers = lines[0][:-1].split(",") #get the numbers we need to draw as a list 
    bingo_cards = get_bingo_cards(lines[2:]) #get the bingo cards, as list of numpy arrays
    answer = task(draw_numbers, bingo_cards) #pass these to whichever task function
   
    file.close()
    return answer

#Returns list of bingo cards as 2d np arrays
def get_bingo_cards(lines, n = BINGO_N):
    
    bingo_cards = []
    
    for line in range(0, len(lines), n+1): 
        #iterate through each line of bingo card in list comprehension; make list for line with .split() and filter out None types
        card = [list(filter(None, lines[x][:-1].split(" "))) for x in range(line, line+n)] 
        bingo_cards.append(np.asarray(card, dtype=int))
                        
    return bingo_cards
    


### TASK ONE ###
#Takes the  list of drawn numbers, and list of np array bingo cards; deduces score of winning card
def task_one(draw_numbers, bingo_cards):
  
    for number in draw_numbers: 
        for card in bingo_cards:  
                  
            if int(number) in card: 
                position = np.where(card == int(number)) #find position in card so we can "strike it off"
                card[position[0][0]][position[1][0]] = -1 #set to -1. bingo only uses positive numbers, so we know its struck off
                
                #so if a row/column sums up to -5, then all are marked off - bingo!
                if -1*BINGO_N in np.sum(card, axis=0) or -1*BINGO_N in np.sum(card, axis=1): 
                    return sum(card[card >= 0]) * int(number)  
          
                
          
### TASK TWO ###
#Takes the list of drawn numbers, and list of np array bingo cards; deduces the score of the last card to bingo
def task_two(draw_numbers, bingo_cards):
 
    for number in draw_numbers:
        
        #keep track of card index(es); we use these to pop off cards from bingo_cards list, when we hit bingo
        card_index, indexes = 0, [] 
    
        for card in bingo_cards:
        
            if int(number) in card: 
                position = np.where(card == int(number)) #find position in card so we can "strike it off"
                card[position[0][0]][position[1][0]] = -1 #set to -1. bingo only uses positive numbers, so we know its struck off
                
                #so if a row/column sums up to -5, then all are marked off - bingo!
                if -1 *BINGO_N in np.sum(card, axis=0) or -1*BINGO_N in np.sum(card, axis=1): 
                    
                    #note: we can't remove bingo'd cards immediately, as it screws up indexing 
                    if len(bingo_cards) != 1: indexes.append(card_index) #so if not last card, note down index to remove it later
                    else: return sum(card[card >= 0]) * int(number)  #otherwise, hurray - now return the score
                    
            card_index += 1
        
        #reverse list, so we don't mess up indexing 
        for index in sorted(indexes, reverse=True): bingo_cards.pop(index)


### PRINTING SOLUTIONS ###
def print_solutions():
    print("Task one:", do_task(task_one))
    print("Task two:", do_task(task_two))
     

print_solutions()  