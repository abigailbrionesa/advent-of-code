from collections import deque

def timelines(row,col,grid,memo):
    #base case
    if col < 0 or col >= len(grid[0]):
        return 0
    if row == len(grid):
        return 1
    if (row,col) in memo:
        return memo[(row,col)]
    if grid[row][col] == '.':
        result = timelines(row+1, col,grid,memo)
    elif grid[row][col] == '^':
        result = timelines(row+1,col-1,grid,memo) + timelines(row+1, col+1,grid,memo)
    else:
        result = timelines(row+1, col, grid, memo)
    memo[(row,col)] = result
    return result

def find_s(grid):
    for i,c in enumerate(grid[0]):
        if c == 'S':
            return i
    return None

def count_splitting(grid):
    w = len(grid[0])
    h = len(grid)
    start_x = find_s(grid)
    total = timelines(0, start_x, grid, {})
    return total

def main():
    with open("input7.txt") as f:
        grid = f.read().splitlines()
        grid = [list(line) for line in grid]
        count = count_splitting(grid)
        print('count:', count)


if __name__ == "__main__":
    main()
