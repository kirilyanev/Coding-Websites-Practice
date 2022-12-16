tests = int(input())

for test in range(0, tests):
    number = input()
    sticks = 0
    for digit in number:
        if digit == '0' or digit == '6' or digit == '9':
            sticks += 6
        elif digit == '1':
            sticks += 2
        elif digit == '2' or digit == '3' or digit == '5':
            sticks += 5
        elif digit == '4':
            sticks += 4
        elif digit == '7':
            sticks += 3
        elif digit == '8':
            sticks += 7

    if sticks % 2 == 0:
        answer = sticks // 2
        print('1' * answer)
    else:
        answer = sticks // 2 - 1
        print('7'+('1' * answer))
