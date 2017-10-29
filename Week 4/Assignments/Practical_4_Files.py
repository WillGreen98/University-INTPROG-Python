import os as os

def file_In_caps():
    file_Path = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/text.txt")
    for line in file_Path:
        print(line.upper())
    file_Path.close()
