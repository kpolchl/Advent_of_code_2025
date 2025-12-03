def main(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    cnt = 0
    knob = 50
    for line in lines:
        direction = line[0]
        steps = int(line[1:])

        cnt += steps // 100
        steps %= 100

        # if direction == 'L':
        #     steps = steps * (-1)
        #     # crossed the boundary or not
        # if knob + steps >= 100 or knob + steps <= 0:
        #     # if the position was zero no need to count
        #     if knob != 0:
        #         cnt += 1
        # knob += steps
        # knob %= 100

        for _ in range(steps):
            if direction == 'L':
                knob -=1
                if knob < 0:
                    knob = 99
            else:
                knob += 1
                if knob > 99:
                    knob = 0

            if knob == 0:
                cnt += 1

        print(line, end='' )
        print(knob ,cnt)
    print(cnt)

if __name__ == "__main__":
    main("code.txt")
