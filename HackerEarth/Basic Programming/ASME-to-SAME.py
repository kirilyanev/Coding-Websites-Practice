number_of_tests = int(input())
is_same = True

for test in range(0, number_of_tests):

    string_length = int(input())
    string_a = input()
    string_b = input()

    char_counter_a = {}
    char_counter_b = {}

    for char in string_a:
        if char == '?':
            continue
        if char not in char_counter_a:
            char_counter_a[char] = 1
        elif char in char_counter_a:
            char_counter_a[char] += 1

    for char in string_b:
        if char not in char_counter_b:
            char_counter_b[char] = 1
        elif char in char_counter_b:
            char_counter_b[char] += 1

    for key in char_counter_a:
        if key in char_counter_b:
            if char_counter_a[key] != char_counter_b[key]:
                is_same = False
                break

    if is_same:
        print('Yes')
    else:
        print('No')
