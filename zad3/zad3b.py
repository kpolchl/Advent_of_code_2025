def main(file_path):
    result = []
    with open(file_path) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        temp = []
        first = (0,0)
        temp.append(first)
        # print(line)
        flag = True
        for i in range(12):
            maxi = '0'
            index = -1
            # print("range ",temp[i][1]+1 , len(line)-(11-i))
            if flag:
                start = 0
            else:
                start = temp[i][1]+1

            for j in range(start ,len(line)-(11-i)):
                # print(maxi, j)
                if int(line[j]) > int(maxi):
                    maxi = line[j]
                    index = j
            flag = False
            # print('end of search', maxi, index)
            temp.append((maxi, index))

        searched_number = ''
        for i in range(1,len(temp)):
            searched_number += str(temp[i][0])
        result.append(int(searched_number))


    print(result)
    print(sum(result))

if __name__ == "__main__":
    main("input.txt")