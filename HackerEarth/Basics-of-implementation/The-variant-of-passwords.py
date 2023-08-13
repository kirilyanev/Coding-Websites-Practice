tests = int(input())

for test in range(0, tests):
    password_length = int(input())
    password_data = input().split(' ')
    password = input()

    old_password = list(password)

    password_zeroes = int(password_data[0])
    password_ones = int(password_data[1])

    zero_count = old_password.count('0')
    ones_count = old_password.count('1')

    new_password = ''
    replacements = 0

    while password_zeroes != zero_count or password_ones != ones_count:
        if password_zeroes - zero_count > 0:
            if password_zeroes != zero_count:
                for i in range(0, password_length):
                    char = old_password[i]
                    if char == '2':
                        char = '0'
                        old_password[i] = char
                        zero_count += 1
                        break
        else:
            if password_ones - ones_count > 0:
                for i in range(password_length, 0):
                    char = old_password[i]
                    if char == '0':
                        char = '1'
                        old_password[i] = char
                        ones_count += 1
                        break
        if password_ones - ones_count > 0:
            if password_ones != ones_count:
                for i in range(0, password_length):
                    char = old_password[i]
                    if char == '2':
                        char = '1'
                        old_password[i] = char
                        ones_count += 1
                        break

    for x in range(0, password_length):
        pass_char = old_password[x]
        new_char = password[x]
        if pass_char != new_char:
            replacements += 1

    print(replacements)
    print(''.join(old_password))