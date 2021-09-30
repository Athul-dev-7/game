#helper function check all its neighbors and update it to the tempArray
def helper(row, column):
    count     = 0
    neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0),
                (1, 1), (-1, 1), (-1, -1), (1, -1)]
    
    for x, y in neighbors:
        if 0 <= row+y < rows and 0 <= column+x < columns and presentGeneration[row+y][column+x] == 1:
            count += 1
    return count
            
def rules(row,column,count):
    if presentGeneration[row][column] == 1:
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
    
    
if __name__ == '__main__':  
    rows                  = int(input("Enter number of rows : "))
    columns               = int(input("Enter number of columns : "))    
    presentGeneration     = []
    nextGeneration        = [[0 for _ in range(columns)] for _ in range(rows)]
    print("Enter the entries row-wise  ")

    for i in range(rows):                               #taking input from the user
        row = []
        for j in range(columns):
            row.append(int(input("Enter the value : ")))
        presentGeneration.append(row)
    print()


    for row in range(rows):                             #printing the present generation
        for col in range(columns):
            print(presentGeneration[row][col],end=" ")
        print()
    print() 

    for row in range(rows):                             #iterate through the presentGeneration using helper function
        for col in range(columns):
            nextGeneration[row][col] = rules(row, col,helper(row,col))    


    for row in range(rows):                             #printing the next generation 
        for col in range(columns):
            print(nextGeneration[row][col],end=" ")
        print()




    