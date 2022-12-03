# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:11:11 2022

@author: Hannah
"""
import statistics

input_file = open("input", "r")

WIN = 6
DRAW = 3
LOSS = 0

"""
Score matrix of wins / losses
There's probably a better way to do this - but honestly, it's 3x3 so...
"""
SCORE_MATRIX = [[1 + DRAW,  2 + WIN,    3 + LOSS],
                [1 + LOSS,  2 + DRAW,   3 + WIN],
                [1 + WIN,   2 + LOSS,   3 + DRAW]]

#TASK ONE
"""
Deduces score when opponent's is A=ROCK, B=PAPER, C= SCISSORS and (our) choice is X=ROCK, Y= PAPER, Z=SCISSORS
Takes opponent, and our choices as strings; returns score
"""
def round_score_1(opponent, you):
    
    #ord(A) = 65, ord(B) = 66, ord(C) = 67, etc... So we can just convert to 0, 1, 2 for either quite easily
    opponent_choice = ord(opponent) - 65 
    your_choice = ord(you) - 88
    
    #then we just use these to look up in  matrix
    score = SCORE_MATRIX[opponent_choice][your_choice]     
  
    return score
        

#TASK TWO
"""
Deduces score when opponent's is A=ROCK, B=PAPER, C= SCISSORS and (our) choice is X=LOSE, Y=DRAW, Z=WIN
Takes opponent, and our choices as strings; returns score
"""
def round_score_2(opponent,you):
    
    #same as above: we convert to 0, 1, 2 except this time we just take opponent's entire row and compare with ours
    opponent_choice = ord(opponent) - 65
    your_choice = ord(you) - 88     
    
    if your_choice == 0:
        return min(SCORE_MATRIX[opponent_choice]) #if we want to lose choose smallest
    
    elif your_choice == 2:
        return max(SCORE_MATRIX[opponent_choice]) #if we want to win choose largest
    
    else: 
        return statistics.median(SCORE_MATRIX[opponent_choice]) #drawing picks the middle score. median should always work with this scoring system
     

"""
Function that goes through each round in file and deduces overall score
Takes the file, and whichever function we want to use to calculate score for individual rounds 
"""
def total_score(file, function):
    
    total_score = 0
    
    for line in file:
        total_score += function(line[0], line[2]) #each line is formatted wherein 0th char is opponent's choice / 2nd char is our choice
        
    return total_score

total_score(input_file, round_score_2)
    
 
    

 