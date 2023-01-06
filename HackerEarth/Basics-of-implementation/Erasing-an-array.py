tests = int(input())

for test in range(0, tests):
    array_length = int(input())
    array = input().split(' ')
    index_to_delete = 0
    answer = 0

    while len(array) > 0:
        for i in range(0, array_length):
            array_length = len(array)
            if array_length <= i+1:
                answer += 1
                del array[0:array_length]
                break
            curr_element = int(array[i])
            next_element = int(array[i+1])

            if curr_element <= next_element:
                index_to_delete = i + 1
            else:
                if index_to_delete == 0:
                    del array[0]
                    answer += 1
                    break
                del array[0:index_to_delete+1]
                answer += 1
                break
    print(answer)
