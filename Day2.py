
def countPossibilities() -> int:

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
            print(index)
            total += index

    return total

def main():
    print(countPossibilities())

if __name__ == "__main__":
    main()