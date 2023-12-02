# cube.py
import sys, re

inFile = open("2cubeconundrum/cubeinput.txt")
sys.stdout = open("2cubeconundrum/log.txt", "w")

limits = {
        "green": 13,
        "red": 12,
        "blue": 14
}

sum = 0
for line in inFile:
        id = line[line.find(" ")+1:line.find(":")]
        #print(id)
        addId = True
        maxB = 0
        maxR = 0
        maxG = 0
        for word in re.split(r'[,;:]',line)[1:]:
                # check color and number to see if its over
                hand = word.strip()
                color = hand[hand.find(" ")+1:]
                number = int(hand[:hand.find(" ")])
                match color:
                        case "blue":
                                if number > maxB: maxB = number
                        case "green":
                                if number > maxG: maxG = number
                        case "red":
                                if number > maxR: maxR = number
        print("minimum required:"+str(maxB),str(maxG),str(maxR))        
        power = maxB * maxG * maxR
        sum += power
        print(sum)
                #print(color+","+number, end="")
        #print()
        
inFile.close()
