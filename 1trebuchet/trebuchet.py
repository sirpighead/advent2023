import sys
import re

numberDict = {
        "threeight": "3eight",
        "sevenine": 79,
        "eightwo": 82,
        "twone": 21,
        "eighthree": 83,
        "nineight": 98,
        "threeight": 38,
        "sevenine": 79,
        "oneight": 18,
        "fiveight": 58,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
}
file = open("trebinput.txt", "r")
sys.stdout = open("log.txt", "w")
sum = 0
for line in file:
        line.replace
        firstnum = -1
        lastnum = -1
        print(line)
        for key in numberDict:
                line = line.replace(key, str(numberDict[key]))
        print(line)
        for character in line:
                if character.isdigit():
                        if firstnum == -1:
                                firstnum = int(character)
                                print(firstnum, end="")
                        lastnum = int(character) 
        print(lastnum)

        sum += 10*firstnum + lastnum   
        print("sum: " + str(sum))                  
file.close()
