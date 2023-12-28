
def getSum1() -> int:
    f = open("Day1Input.txt", "r")
    f = f.readlines()

    total = 0

    for line in f:
        number = []
        for letter in line:
            if letter.isdigit():
                number.append(letter)
        
        total += int(number[0] + number[-1])
                    
    return total

def getSum2() -> int:
    with open("Day1Input.txt", "r") as file:
        lines = file.readlines()
    
    total = 0

    for line in lines:
        start = None
        end = None
        for index in range(len(line)):
            if line[index].isdigit():
                end = str(line[index]) 

                if not start:
                    start = str(line[index])
            else:
                for id, item in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                    if line[index:].startswith(item):
                        end = str(id + 1)

                        if not start:
                            start = str(id + 1)
        
        total += int(start + end)

    return total
def main():
    print("part 1: " + str(getSum1()))
    print("part 2: " + str(getSum2()))

if __name__ == "__main__":
    main()