# -*- coding: utf-8 -*-
FILE = "input"
PACKET_MARKER, MESSAGE_MARKER = 4, 14


def do_tasks(marker_type, file_name = FILE):
    file = open(file_name, "r")
    for line in file: signal = line[:-1]
    file.close()
    
    for i in range (0, len(signal)):  
        if len(set(signal[i:i+marker_type])) == marker_type: return i+marker_type
 
def print_solutions():
    print("TASK 1:",do_tasks(PACKET_MARKER))
    print("TASK 2:",do_tasks(MESSAGE_MARKER))

print_solutions()