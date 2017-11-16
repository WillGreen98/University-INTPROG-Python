import graphics as g
import time
import math, random as rand

#--------------- Week 6 ----------------------#
def drawCircle(window, centre, radius, colour):
    circle = g.Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(window)


def distanceBetweenPoints(a, b):
    return (math.sqrt((b.getX() - a.getX()) ** 2 + (b.getY() - a.getY()) ** 2))


def drawColouredEye(window, center, radius, colour):
    drawCircle(window, center, radius, "")
    drawCircle(window, center, radius / 2, colour)
    drawCircle(window, center, radius / 4, "black")


def calculateGrade(mark):
    if mark >= 16:
        print('A')
    elif mark >= 12:
        print('B')
    elif mark >= 8:
        print('C')
    elif mark < 8:
        print('F')
    else:
        print('Invalid Input')
#--------------- Week 6 ----------------------#

def trafficLights():
    window = g.GraphWin()

    light_Red = g.Circle(g.Point(100, 50), 20)
    light_Red.setFill("red")
    light_Red.draw(window)

    light_Amber = g.Circle(g.Point(100, 100), 20)
    light_Amber.setFill("black")
    light_Amber.draw(window)

    light_Green = g.Circle(g.Point(100, 150), 20)
    light_Green.setFill("black")
    light_Green.draw(window)

    while True:
        light_Green.setFill("black")
        light_Red.setFill("red")

        time.sleep(1)

        light_Amber.setFill("yellow")
        light_Red.setFill("black")

        time.sleep(1)

        light_Amber.setFill("black")
        light_Green.setFill("green")

        time.sleep(1)

def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

def askaName():
    while True:
        name = input("What is your name: ")

        if name.isnumeric():
            print("Invalid input")
        else:
            break

def calculateCourseWork():
    while True:
        grade = int(input("Enter Mark: "))
        if grade.isnumeric() and grade >= 0 and grade <= 20:
            calculateGrade(grade)
            break
        print("Invalid input")
def orderPrice():
    total = 0
    while True():
        price = float(("Enter Price: £"))
        if price.isnumeric():
            volume = int(input("Enter volume: "))
            if volume.isnumeric():
                total += (price * volume)

                usr_In = input("Continue: ".lower())
                if usr_In == 'n' or usr_In == "no":
                    break

def clickEye():
    window = g.GraphWin("Clickable Eye", 400, 400)
    drawColouredEye(window, g.Point(200, 200), 100, "green")

    text = g.Text(g.Point(50, 50), "").draw(window)

    while True:
        click = window.getMouse()
        distance = distanceBetweenPoints(click, g.Point(200, 200))

        if distance <= 25:
            text.setText("Pupil")
        elif distance <= 50:
            text.setText("Iris")
        elif distance <= 100:
            text.setText("Sclera")
        else:
            break

def temperatureConverter():
    while True:
        temp_In = input("Enter temp C/F: ")

        if temp_In is not None:
            temp = temp_In.split[0:1]
            if 'c' in temp:
                celsius2Fahrenheit(temp)
            elif 'f' in temp:
                fahrenheit2Celsius(temp)
            else:
               break
        else:
            print("Invalid input")
            break

def guessNumber():
    gussed = False
    rand_Num = rand.randint(0, 50)

    for guess_Counter in range(0, 10):
        guess = int(input("Enter guess: "))

        if guess < rand_Num:
            print("Too Low")
        elif guess > rand_Num:
            print("Too High")
        elif guess == rand_Num:
            print("Correct, you guessed in: ", guess_Counter, " tries")
            gussed = True
            break
    if gussed == False:
        print("Too many guesses")

def tableTennisScorer():
    window = g.GraphWin("Table Tennis")

    player_One_Score = 0
    player_Two_Score = 0

    player_One_Text = g.Text(g.Point(50, 50), "0").draw(window).setSize(12)
    player_Two_Text = g.Text(g.Point(100, 50), "0").draw(window).setSize(12)
    player_One_Win_Text = g.Text(g.Point(50, 75), "").draw(window).setSize(12)
    player_Two_Win_Text = g.Text(g.Point(150, 75), "").draw(window).setSize(12)

    boarder_Reft = g.Rectangle(g.Point(0, 0), g.Point(100, 200)).draw(window)
    boarder_Right = g.Rectangle(g.Point(0, 0), g.Point(200, 200)).draw(window)

    while True:
        click = window.getMouse()

        if click.getX() > 100:
            player_Two_Score += 1
        else:
            player_One_Score += 1

        if player_One_Score > 10 and player_One_Score > player_Two_Score:
            player_One_Win_Text.setText("Player One Wins")
            break

        if player_Two_Score > 10 and player_Two_Score > player_One_Score:
            player_Two_Win_Text.setText("Player Two Wins")
            break

        player_One_Win_Text.setText(player_One_Score)
        player_Two_Win_Text.setText(player_Two_Score)

    window.getMouse()

def clickableBoxOfEyes(row, col):
    window = g.GraphWin("")

temperatureConverter()