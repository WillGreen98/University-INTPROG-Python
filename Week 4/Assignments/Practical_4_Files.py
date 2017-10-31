import graphics as g
import random

def file_In_caps():
    file_Path = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/text.txt")
    for line in file_Path:
        print(line.upper())
    file_Path.close()

def rainFallChart():
    file_Path_Rain_txt = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/rainfall.txt")
    for line in file_Path_Rain_txt:
        print(line.split()[0], "*" * int(line.split()[1]))

def graphicalRainfallChart():
    file_Path_Rain_txt = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/rainfall.txt")

    window = g.GraphWin("Rain fall Graph", 400, 400)

    for i, line in file_Path_Rain_txt:
        volume = int(line.split()[1])

        rectangle = g.Rectangle()


        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        rand_Color = g.color_rgb(r, g, b)

