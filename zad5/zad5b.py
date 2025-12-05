import sys

def intercepts(range1, range2):
    print(range1, range2)
    if range1[1] >= range2[0]:
        return True
    else:
        return False

def main(file_path):
    file = open(file_path, 'r')
    ranges= []
    flag = False
    fresh_cnt = 0
    for line in file:
        line = line.strip('\n')
        if line == '':
            break

        line = line.split('-')
        beginnig = int(line[0])
        ending = int(line[1])
        ranges.append([beginnig, ending])

    ranges.sort()
    print(ranges)
    result_ranges = []
    result_ranges.append(ranges[0])
    current_index = 0
    for i in range(1, len(ranges)):
        if intercepts(result_ranges[current_index], ranges[i]):
            result_ranges[current_index] = [min(result_ranges[current_index][0], ranges[i][0]), max(result_ranges[current_index][1], ranges[i][1])]
        else:
            result_ranges.append(ranges[i])
            current_index +=1
    result_num = 0
    print(result_ranges)
    for r in result_ranges:
        result_num += r[1] - r[0] + 1
    print(result_num)



if __name__ == '__main__':
    main('input.txt')