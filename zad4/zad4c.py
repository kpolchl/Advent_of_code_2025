def pret_print(table):
    for row in table:
        print(row)
def check_adjacent(grid, x,y):
    cnt = 0
    for y1 in range(y-1,y+2):
        for x1 in range(x-1,x+2):
            if x1 == x and y1 == y:
                continue
            if grid[y1][x1] == 1:
                cnt += 1
    # pret_print(grid)
    return cnt


def main(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    grid = []
    grid.append([0]*(len(lines)+2)) # just for checking adjacent minimize checks
    for line in lines:
        line = line.strip('\n')
        temp = []
        temp.append(0) # just for checking adjacent minimize checks
        for i in line:
            if i == '@':
                temp.append(1)
            else:
                temp.append(0)
        temp.append(0) # just for checking adjacent minimize checks
        grid.append(temp)

    grid.append([0]*(len(lines)+2)) # just for checking adjacent minimize checks
    # pret_print(grid)

    result = 0
    # brute force xd brutalna sila time
    while True:
        prev = 0
        for x in range(1,len(grid)-1):
            for y in range(1,len(grid)-1):
                if grid[y][x] == 1:
                    if check_adjacent(grid, x, y) < 4:
                        print(x,y)
                        result += 1
                        prev += 1
                        grid[y][x] = 0

        if prev ==0:
            break



    print(result)
    # pret_print(grid)

if __name__ == '__main__':
    main('input.txt')