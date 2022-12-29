tests = int(input())

for test in range(0, tests):
    string = input()
    character = input()
    answer = 0

    for char in string:
        if char == character:
            answer += 1

    print(answer)
