number_of_tests = int(input())

for test in range(0, number_of_tests):
    is_possible = True
    string_length = int(input())
    string_a = input()
    string_b = input()

    for char in string_a:
        if char == '?':
            continue
        elif char not in string_b:
            is_possible = False

    if is_possible:
        print('Yes')
    else:
        print('No')
