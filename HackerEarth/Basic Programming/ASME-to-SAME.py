number_of_tests = int(input())

for test in range(0, number_of_tests):

    string_length = int(input())
    string_a = input()
    string_b = input()

    result_a = ''.join(sorted(string_a, reverse=True))
    result_b = ''.join(sorted(string_b, reverse=True))

    count_a = 0
    count_b = 0

    for i in range(0, string_length):
        char = result_a[i]
        if char in result_b:
            result_a = result_a.replace(char, '1')
            result_b = result_b.replace(char, '1')
        #if char == '?':
        #    result_b = result_b.replace(result_b[i], '1')

        for char in result_a:
            if char == '1':
                count_a += 1
        for char in result_b:
            if char == '1':
                count_b += 1
    result_a = result_a.replace('?', '1')

    if count_a == count_b:
        print('Yes')
    else:
        print('No')
