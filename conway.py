board     = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1],
             [0, 0, 0]
             ]
rows      = len(board)
columns   = len(board[0])
tempArray = [[0 for _ in range(columns)] for _ in range(rows)]


def helper(row, column):
    count     = 0
    neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0),
                (1, 1), (-1, 1), (-1, -1), (1, -1)]
    
    for x, y in neighbors:
        if 0 <= row+y < rows and 0 <= column+x < columns and board[row+y][column+x] == 1:
            count += 1

    if board[row][column] == 1:
        if count < 2:
            return 0
        elif count in [2, 3]:
            return 1
        else:
            return 0

    else:
        if count == 3:
            return 1
        else:
            return 0


def nextGeneration():
    for row in range(rows):
        for col in range(columns):
            tempArray[row][col] = helper(row, col)
    return tempArray


if __name__ == '__main__':
    print(tempArray)
    print(nextGeneration())
