import sys

def is_between(num , a, b):
    if num < a:
        return False
    elif num > b:
        return False
    else:
        return True


def main(file_path):
    file = open(file_path, 'r')
    ranges= []
    flag = False
    fresh_cnt = 0
    for line in file:
        line = line.strip('\n')
        if line == '':
            flag = True
            continue
        if not flag:
            line = line.split('-')
            beginnig = int(line[0])
            ending = int(line[1])
            ranges.append((beginnig, ending))
        else:
            for r in ranges:
                if is_between(int(line), r[0], r[1]):
                    fresh_cnt += 1
                    break
    print(fresh_cnt)

if __name__ == '__main__':
    main('input.txt')