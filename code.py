import os

file = "expenses.txt"


def add():
    thing = input("what did you buy: ")
    amt = input("how much: ")
    cat = input("type (food/travel/other): ")

    try:
        f = open(file, "a")
        line = thing + "|" + amt + "|" + cat + "\n"
        f.write(line)
        f.close()
    except:
        print("problem saving")

    print("done")


def show():
    if os.path.exists(file) == False:
        print("nothing added yet")
        return

    print("\n--- list ---\n")

    f = open(file)

    for l in f:
        parts = l.strip().split("|")

        if len(parts) == 3:
            print(parts[0], "-", parts[1], "rs")
    f.close()


def total():
    if not os.path.exists(file):
        print("no data")
        return

    s = 0

    f = open(file)

    for l in f:
        try:
            s = s + int(l.split("|")[1])
        except:
            print("", end="")   # ignore bad lines

    f.close()

    print("total =", s)


def catwise():
    if not os.path.exists(file):
        print("empty")
        return

    f = open(file)

    food = 0
    travel = 0
    other = 0

    for l in f:
        data = l.strip().split("|")

        if len(data) < 3:
            continue

        try:
            money = int(data[1])
        except:
            continue

        if data[2] == "food":
            food += money
        elif data[2] == "travel":
            travel += money
        else:
            other += money

    f.close()

    print("\nfood:", food)
    print("travel:", travel)
    print("other:", other)


def budget():
    limit = 5000

    if not os.path.exists(file):
        print("no records")
        return

    t = 0
    f = open(file)

    for l in f:
        try:
            t += int(l.split("|")[1])
        except:
            pass

    f.close()

    if t > limit:
        print("too much spending!")
    else:
        print("ok for now")


# following is the main loop 
while True:
    print("\n1 add")
    print("2 show")
    print("3 total")
    print("4 category")
    print("5 budget")
    print("6 exit")

    c = input("choose: ")

    if c == "1":
        add()
    elif c == "2":
        show()
    elif c == "3":
        total()
    elif c == "4":
        catwise()
    elif c == "5":
        budget()
    elif c == "6":
        break
    else:
        print("invalid")
