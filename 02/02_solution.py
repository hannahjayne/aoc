 FILE_NAME = "input"
LOSS, DRAW, WIN = 0, 3, 6 

"""
Goes through each "round" in file and deduces overall score
Takes the file, and whichever function we want to use as parameters; returns overall score 
"""
def total_score(file_name, function):
    
    file = open(file_name, "r")
    
    total_score = 0
    
    for line in file:
        total_score += function(line[0], line[2]) #each line is formatted wherein 0th char is opponent's choice / 2nd char is our choice
        
    return total_score

    file.close()


"""
Deduces the score for each round, subject to problem one's condition's
That is: opponent's A=Rock, B=Paper, C=Scissors and [your choice] is X=Rock, Y=Paper, Z=Scissors
"""
def problem_one(opponent, you):
    
    #bit cheeky, but uses ord() to get unicode number - so for example ord("A") = 65, ord("B") = 66, etc...
    #then subtraction sets it to 0 for rock, 1 for paper, 2 for scissors - for either player
    opponent_choice =  ord(opponent) - 65 
    your_choice = ord(you) - 88
    
     
    if opponent_choice == your_choice:  #if we have the same numbers then its a draw
        return DRAW + your_choice + 1 
    
    #now the idea here is 0 = rock, paper = 1, scissors = 2... so each choice is beat by the consecutive number 
    #hence if opponent's choice + 1 = your choice, you win
    elif (opponent_choice + 1) % 3 == your_choice: 
        return WIN + your_choice + 1
    
    #otherwise, if the two other conditions arent met there's one option left and you've lost 
    else: 
        return LOSS + your_choice +1
         
"""
Deduces the score for each round, subject to problem two's condition's
That is: opponent's A=Rock, B=Paper, C=Scissors and [your choice] is X=Lose, Y=Draw, Z=Win
"""
def problem_two(opponent, you):
    
    #same reasoning as in problem_one, but now 0 = loss, 1 = draw, 2 = win as stated for your_choice
    opponent_choice = ord(opponent) - 65
    your_choice = ord(you) - 88 
    
    #following the same logic as problem_one() but reverse engineering it
    
    if your_choice == 0:
        return LOSS + (opponent_choice - 1) % 3 + 1 #so to lose, we'd pick the option "before" opponent's choice
    
    elif your_choice == 1:
        return DRAW + opponent_choice + 1 #then to draw we just pick opponent's choice
    
    else:
        return WIN + ((opponent_choice + 1) %3) + 1 #then to win we'd pick the option "after" opponent's choice
    
    
print(total_score(FILE_NAME, problem_one))
print(total_score(FILE_NAME, problem_two))
