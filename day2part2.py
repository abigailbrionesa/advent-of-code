# gift shop

def is_invalid(input):
    str_input = str(input)
    n = len(str_input)
    if len(str_input) < 2:
        return False
    return str_input in (str_input + str_input)[1:-1]
        

def invalid_sum(input):
    total = 0
    for id in input:
        if is_invalid(id):
            total += id
    return total
    
def main():
    with open("input2.txt") as f:
        line = f.read().strip()
    ids = []
    for group in line.split(','):
        a,b = group.split('-')
        for ids_range in range(int(a), int(b)+1):
            ids.append(ids_range)
    result = invalid_sum(ids)
    print("invalid count:", result)

if __name__ == "__main__":
    main()
