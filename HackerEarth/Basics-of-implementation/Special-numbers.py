integers = int(input())
special_numbers = []
answer = 0


def f(v):
    if v > integers:
        return
    if v > 0:
        special_numbers.append(v)
    f(10 * v + 4)
    f(10 * v + 7)


f(4)
f(7)

if len(special_numbers) > 0:
    first_num = special_numbers.pop(0)

result = []

while len(special_numbers) > 0:
    for current_number in special_numbers:
        def gcd(p, q):
            # Create the gcd of two positive integers.
            while q != 0:
                p, q = q, int(p) % int(q)
            return p


        def is_coprime(x, y):
            return gcd(x, y) == 1

        if is_coprime(current_number, first_num):
            answer += 1

    first_num = special_numbers.pop(0)

print(answer)
