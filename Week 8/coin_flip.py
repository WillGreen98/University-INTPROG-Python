import random as rand

def getInputs():
    while True:
        n_flips = int(input("How many coin flips: "))

        if n_flips.isnumeric():
            return n_flips

def flip(index):
    flips = []
    for i in range(index):
        flips.append(rand.randint(0, 1))
    return flips


def results(result):
    head_counter = result.count(0) / 100
    tail_counter = result.count(1) / 100

    print("Heads: ", head_counter, " Tails: ", tail_counter)

def main():
    index = getInputs()
    flips = flip(index)
    results(flips)

if __name__ == '__main__':
    main()