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
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        rand_Color = g.color_rgb(r, g, b)

        volume = int(line.split()[1])

        rectangle = g.Rectangle().draw(window).setFill(rand_Color)
        text = g.Text(g.Point()).draw(window).setSize(10)

    window.getMouse()
    file_Path_Rain_txt.close()

def rainFall_Inches():
    file_Path_Rain_txt = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/rainfall.txt")
    rainFile_Inches = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/rainFile_Inches.txt")

    with open(file_Path_Rain_txt) as file:
        for line in file:
            inches = int(line.split()[1]) / 25.4
            rainFile_Inches.write(inches, "\n")

    rainFile_Inches.close()

def wc():
    line_Count = 0
    word_Count = 0
    character_Count = 0

    file_Quote = open("/Users/Will/Desktop/Uni/INTPROG/Practicals/Week 4/Assignments/quotation.txt")

    with open(file_Quote) as file:
        for line in file_Quote:
            line_Count += 1
            word_Count += 1
            character_Count += 1

    print("Line Count:", line_Count, "\n",
          "Word Count:", word_Count, "\n",
          "Character Count:", character_Count)
