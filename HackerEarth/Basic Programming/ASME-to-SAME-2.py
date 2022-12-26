number_of_tests = int(input())
question = '?'

for test in range(0, number_of_tests):

    string_length = int(input())
    string_a = input()
    string_b = input()

    result_a = ''.join(sorted(string_a))
    result_b = ''.join(sorted(string_b))

    if question in result_a:
        index_of_question = result_a.index(question)
        questions_count = result_a.count(question)
        substring_a = result_a[index_of_question:questions_count]
        result_a = result_a.replace(substring_a, '')

    if result_a in result_b:
        print('Yes')
    else:
        print('No')
