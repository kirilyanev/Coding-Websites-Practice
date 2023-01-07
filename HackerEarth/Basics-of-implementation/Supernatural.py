number = int(input())
answer = 0

for num in range(1, 1000000):
    result = 1
    if '1' in str(num) or '0' in str(num):
        continue
    for digit in str(num):
        result *= int(digit)
    if result == number:
        answer += 1

print(answer)
