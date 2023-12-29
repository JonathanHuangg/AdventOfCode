def getParts1() -> int:
    arr = []
    with open("Day3Input.txt", "r") as file:
        for line in file:
            arr.append(line.strip())

    totalRows = len(arr)
    totalCols = len(arr[0])
    visited = set()
    total = 0

    def search(row, col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        nonlocal total
        for direction in directions:
            newRow = row + direction[0]
            newCol = col + direction[1]
            if totalRows > newRow >= 0 and totalCols > newCol >= 0 and arr[newRow][newCol].isdigit():

                left,right = newCol, newCol

                while left > 0 and arr[newRow][left - 1].isdigit():
                    
                    left -= 1

                while right < totalCols and arr[newRow][right].isdigit():
                    right += 1

                # numbers are not unique so I will use the coordinate of the leftmost number
                
                if (newRow, left) not in visited:
                    number = arr[newRow][left : right]
                    print(number)
                    total += int(number)
                    visited.add((newRow, left))

    for row in range(totalRows):
        for col in range(totalCols):
            if arr[row][col] != '.' and not arr[row][col].isdigit():
                search(row, col)
    return total

def main():
    print(getParts1())

if __name__ == "__main__":
    main()