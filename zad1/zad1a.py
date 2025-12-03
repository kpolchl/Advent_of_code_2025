def main(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    cnt = 0
    knob = 50
    for line in lines:
        if line[0] == 'L':
            numb = int(line[1:])
            knob -= numb
        else:
            numb = int(line[1:])
            knob += numb
        if knob < 0:
            knob = 100 + knob
        knob %= 100
        if knob == 0:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main("code.txt")
