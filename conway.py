from time import sleep


def get_live_neighbours_count(row, column, present_generation):
    """Returns the number of live neighbours"""
    
    rows       = len(present_generation)
    columns    = len(present_generation[0])
    count      = 0
    neighbours = [(0, 1), (0, -1), (-1, 0), (1, 0),
                (1, 1), (-1, 1), (-1, -1), (1, -1)]
    
    for x, y in neighbours:
        if 0 <= row+y < rows and 0 <= column+x < columns and present_generation[row+y][column+x] == 1:
            count += 1
    return count

def apply_4_rules(row, column, count, present_generation):
    """
    1. Any live cell (1) with fewer than two live neighbours dies (0), as if by underpopulation.
    2. Any live cell (1) with two or three live neighbours lives (1) on to the next generation.
    3. Any live cell (1) with more than three live neighbours dies (0), as if by overpopulation.
    4. Any dead cell (0) with exactly three live neighbours becomes a live cell (1), as if by reproduction.
    """
    
    if present_generation[row][column] == 1:
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
        
def generate_next_generation(rows, columns, present_generation):
    """Returns the next generation"""
    
    next_generation = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):                             
        for j in range(columns):
            count = get_live_neighbours_count(i, j, present_generation)
            next_generation[i][j] = apply_4_rules(i, j, count, present_generation)

    if next_generation == present_generation:
        pass
    else:
        sleep(1)
        display_generation(rows, columns,next_generation)
        generate_next_generation(rows, columns, next_generation)
        

def display_generation(rows, columns, generation):
    for i in range(rows):                             
        for j in range(columns):
            print(generation[i][j],end="  ")
        print()
    print() 

def main():
    present_generation = [[0, 1, 0],
                          [0, 0, 1],
                          [1, 1, 1],
                          [0, 0, 0]]
    rows               = len(present_generation)
    columns            = len(present_generation[0])
    display_generation(rows, columns, present_generation)
    generate_next_generation(rows, columns, present_generation)
    
if __name__ == '__main__':
    main()
