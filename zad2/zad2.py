import sys
from math import log10 , ceil
def check_num(num):
    length = int(log10(num))+1
    # print(length)
    if length % 2 ==1:
        return True
    else:
        half1 = num%(10**(length//2))
        half2 = num//(10**(length//2))
        # print(half1, half2)
        if half1 == half2:
            return False
        return True

def check_num2(num):
    length = int(log10(num))+1
    temp_num = num

    for i in range(1,length//2+1):
        if length % i != 0:
            continue

        temp_num = num
        while True:
            prev = temp_num %(10 ** i)
            temp_num = temp_num//(10 ** i)
            current = temp_num%(10 ** i)
            # print(prev, current ,temp_num )
            if temp_num == 0:
                flag = False
                return False
            if current != prev:
                break

    return True


def main(file_path):
    with open(file_path, 'r') as f:
        line = f.readline().split(',')
        # print(line)
        parsed = []
        for r in line:
            r = r.split('-')
            parsed.append((int(r[0]), int(r[1])))

        result = 0
        for part in parsed:
            prev = part[0]
            nexta = part[1]
            # print(prev, nexta)
            if prev<nexta:
                for num in range(prev, nexta+1):
                    if not check_num2(num):
                        print(num)
                        result += num
    print(result)


if __name__ == "__main__":
    # print(check_num2(10101))
    main("input.txt")
