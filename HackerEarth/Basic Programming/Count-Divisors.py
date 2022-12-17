numbers = input().split(' ')
divider = int(numbers[2])
count = 0

for x in range(int(numbers[0]), int(numbers[1]) + 1):
    if x % divider == 0:
        count += 1

print(count)