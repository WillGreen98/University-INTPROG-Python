class person:
    def __init__(self, name):
        self.name = name


Will = person.name = "Will"

def killMyself(name):
    person.name = name
    mystr = " is now dead"

    killed = print("{0}{1}".format(name, mystr))
    return killed

def main():
    killMyself(Will)

if __name__ == '__main__':
    main()