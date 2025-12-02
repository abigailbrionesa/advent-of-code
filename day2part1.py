# gift shop

def is_invalid(input):
    str_input = str(input)
    n = len(str_input)
    left = str_input[:(n//2)]
    right = str_input[(n//2):n]
    if left[0] == '0' or right[0] == '0':
        return False
    return left == right

def invalid_count(input):
    count = 0
    for id in input:
        if is_invalid(id):
            count +=1
    return count
    
def main():
    with open("input2.txt") as f:
        line = f.read().strip()
        ids = []
        for group in line.split(','):
            a,b = group.split('-')
            ids.append(int(a))
            ids.append(int(b))
    result = invalid_count(ids)
    print("invalid count:", result)

if __name__ == "__main__":
    main()
