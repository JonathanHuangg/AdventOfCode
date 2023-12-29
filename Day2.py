import math
def countPossibilities1() -> int:

    with open("Day2Input.txt", "r") as file:
        lines = file.readlines()

    LIMITS = {"r" : 12, "g" : 13, "b" : 14}
    total = 0

    for line in lines:
        index = int(line[5 : line.index(":")])

        subGames = line.split(':')[1].split(";") # first split by :, get second part, then by ;
        
        continueLine = True
        currGame = {"r" : 0, "b" : 0, "g" : 0}

        for subset in subGames:

            colors = subset.split(",")

            for color in colors:
                count, color = color.strip().split() # split based on whitespace
                currGame[color[0]] = int(count)
        
            for key, value in currGame.items():
                print(key, value, LIMITS[key])
                if value > LIMITS[key]:
                    continueLine = False
                    break
            
            if not continueLine:
                break
                    
        if continueLine:
            total += index

    return total

def countPossibilities2() -> int:
    with open("Day2Input.txt", "r") as file:
        lines = file.readlines()
    
    total = 0
    
    # Game 1: 
    for line in lines:
        currColors = {"r" : 0, "b" : 0, "g" : 0}

        #12 blue; 2 green, 13 blue, 19 red; 13 red, 3 green, 14 blue
        subsections = line.split(':')[1].split(";")
        
        # 2 green, 13 blue, 19 red
        for subset in subsections:
            colors = subset.split(",")
            for color in colors:
                # 2     green
                count, color = color.strip().split()
                currColors[color[0]] = max(currColors[color[0]], int(count))
        
        total += math.prod(currColors.values())
    return total

def main():
    print(countPossibilities1())
    print(countPossibilities2())

if __name__ == "__main__":
    main()