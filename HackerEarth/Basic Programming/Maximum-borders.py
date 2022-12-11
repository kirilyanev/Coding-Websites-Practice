test_cases = int(input())

for test in range(0, test_cases):
    matrix = input().split()
    results = []
    for row in range(0, int(matrix[0])):
        curr_test = input()
        count = 0
        for char in curr_test:
            if char == '.':
                count = 0
            if char == '#':
                count += 1
                results.append(count)
    print(max(results))
