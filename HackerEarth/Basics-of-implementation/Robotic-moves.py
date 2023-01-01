tests = int(input())

for test in range(0, tests):
    moves = int(input())
    answer = moves * (moves + 1)
    print(answer)
