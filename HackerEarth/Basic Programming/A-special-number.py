number_of_tests = int(input())


def special_num(num):
    count = 0
    for digit in str(num):
        count += int(digit)
    if count % 4 == 0:
        return num
    else:
        return special_num(num + 1)


for test in range(0, number_of_tests):
    number = int(input())
    result = special_num(number)

    print(result)
