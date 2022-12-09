word = input()
x = 0
y = 0

for char in word:
    if char == 'z':
        x += 1
    elif char == 'o':
        y += 1


if 2 * x == y:
    print('Yes')
else:
    print('No')
