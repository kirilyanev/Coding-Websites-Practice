""" My solution:

tests = int(input())

for test in range(0, tests):
    array_length = int(input())
    array = input().split(' ')

    first_index = {}
    last_index = {}

    received_numbers = []

    for i in range(0, array_length):
        current_number = array[i]
        index = i

        if current_number not in received_numbers:
            first_index[current_number] = index
            last_index[current_number] = index
        else:
            last_index[current_number] = index

        received_numbers.append(current_number)

    answer = 0

    for key in first_index.keys():
        answer += abs(last_index[key]) - abs(first_index[key])

    print(answer)
"""

# Very clever solution with the help of the comments in HackerEarth
tests = int(input())

for test in range(0, tests):
    array_length = int(input())
    array = input().split()

    dictionary = {}
    answer = 0

    for i in range(0, array_length):
        if array[i] in dictionary:
            answer += i - dictionary[array[i]]
            dictionary[array[i]] = i
        else:
            dictionary[array[i]] = i
    print(answer)
