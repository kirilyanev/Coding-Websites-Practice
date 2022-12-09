word = input()
vowels = 'AEIOUY'
is_valid = True

if word[2] in vowels:
    is_valid = False

test_one = int(word[0]) + int(word[1])
test_two = int(word[3]) + int(word[4])
test_three = int(word[4]) + int(word[5])
test_four = int(word[7]) + int(word[8])

if test_one % 2 != 0 or test_two % 2 != 0 or test_three % 2 != 0 or test_four % 2 != 0:
    is_valid = False

if is_valid:
    print('valid')
else:
    print('invalid')
