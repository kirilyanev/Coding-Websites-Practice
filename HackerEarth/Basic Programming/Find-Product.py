numbers_count = int(input())
numbers = input().split()
answer = 1

for i in range(0, numbers_count):
    answer = (answer * int(numbers[i])) % (1000000000 + 7)

print(answer)
