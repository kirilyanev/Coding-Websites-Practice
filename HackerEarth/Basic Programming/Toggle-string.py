string = input()
result = ''

for char in string:
    if char == char.lower():
        result += char.upper()
    elif char == char.upper():
        result += char.lower()

print(result)
