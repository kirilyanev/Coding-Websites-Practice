number_of_tests = int(input())
is_same = True
question = '?'

for test in range(0, number_of_tests):

    string_length = int(input())
    string_a = input()
    string_b = input()

    result_a = ''.join(sorted(string_a))
    result_b = ''.join(sorted(string_b))

    questions_count = 0

    for i in range(0, string_length):
        char = result_a[i]

        if char != question and char not in result_b:
            is_same = False
        elif char == question and question in result_a:
            questions_count += 1

    if question in result_a:
        index_of_question = result_a.index(question)

    substring_a = result_a[int(index_of_question):questions_count]
    substring_b = result_b[int(index_of_question):questions_count]
    result_a = result_a.replace(substring_a, '')
    result_b = result_b.replace(substring_b, '')

    if result_a == result_b:
        print('Yes')
    else:
        print('No')
