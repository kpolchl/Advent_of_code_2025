
def main(file_path):
    result = []
    with open(file_path) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        first_num = 0
        first_num_idx = -1
        second_num = 0
        for i in range(len(line)-1):
            if int(line[i]) > first_num:
                first_num = int(line[i])
                first_num_idx = i

        for j in range(first_num_idx+1, len(line)):
            if int(line[j]) > second_num:
                second_num = int(line[j])

        searched = 10*first_num + second_num
        result.append(searched)

    print(result)
    print(sum(result))

if __name__ == "__main__":
    main("input.txt")