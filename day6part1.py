#trash compactor
def main():
    with open("input6example.txt") as f:
        content = f.read()
    grid = [list(line) for line in content.splitlines()]
    h = len(grid)
    w = len(grid[0])
    operators = []
    
    for k in grid[-1]:
        if k =='+' or k=='*':
         operators.append(k)
        
    print(operators)
    
    cursor = w-1
    results = []
    
    while cursor >= 0:
        operator = operators.pop()
        for _ in range(3):
            curr = ''
            if operator == '*':
                result = 1
            elif operator == '+':
                result = 0
            for j in range(h-1):
                curr += grid[j][cursor]
            cursor -= 1
            if operator == '*':
                result *= int(curr) 
            elif operator == '+':
                result += int(curr)
            print('complete')
        results.append(result)
        print('__')
        cursor -= 1
    print(results)
              
            
            
if __name__ == "__main__":
    main()