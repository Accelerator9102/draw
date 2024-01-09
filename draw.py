
import random


def randomInt(maxvalue):
    return random.randint(1, maxvalue)

def draw(numOfPrize, totalAttendant):
    list0 = []
    # duplicate  = False
    for i in range(numOfPrize):
        ranint = randomInt(totalAttendant)
        while ranint in list0:
            ranint = randomInt(totalAttendant)
        list0.append(ranint)

    return list0
        # if ranint in list0:
        #     duplicate = True
        #     while duplicate:
        #         duplicate = list0.contains(randomInt(totalAttendant))

def main():
    nump = int(input("Enter Prize Count: "))
    total = int(input("Enter Total Attendants: "))

    for el in draw(nump, total):
        print(el)

main()