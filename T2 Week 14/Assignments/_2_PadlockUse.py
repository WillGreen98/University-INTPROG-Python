from _6_padlock import Padlock
import random as rand

def main():
    code = rand.randint(0, 100)
    padlock = Padlock(code)
    print(code)
    
    for i in range(15, -1, -1):
        guess = input("Guess the code to open the padlock: ")
        if guess.isdigit():
            padlock.open(int(guess))
            if not padlock.isLocked:
                print("Code is correct, it took you", 16 - i, "guesses." if i < 15 else "guess.")
                break
        else:
            print("Wrong. (Also, code is a number)")
        print("Number of guesses left:", i)
    
main()