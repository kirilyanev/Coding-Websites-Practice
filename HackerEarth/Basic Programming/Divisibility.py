array_length = int(input())
array = input().split(' ')
result = []

for i in range(0, array_length):
    last_digit = int(array[i]) % 10
    result.append(str(last_digit))

result = ''.join(result)

if int(result) % 10 == 0:
    print('Yes')
else:
    print('No')
