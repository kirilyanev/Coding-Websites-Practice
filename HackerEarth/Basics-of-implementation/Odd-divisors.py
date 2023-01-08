# my try for solution(not working). Not sure about the description of the problem

# tests = int(input())

# for test in range(0, tests):
#    input_data = input().split()
#    number = int(input_data[0])
#    divider = int(input_data[1])
#    total_sum = 0

#   i = 1

#    while i <= number:
#        if number % i == 0:
#            total_sum += i
#        i += 2

#    result = total_sum % divider
#    print(result)

# working solution, still not sure how it works(description not clear)
for i in range(int(input())):
    n, m = map(int, input().split())
    ans = 0

    while 1:
        ans += (((n // 2 + n % 2) % m) * ((n // 2 + n % 2) % m)) % m
        ans = ans % m

        n = n // 2

        if n == 0:
            break

    print(ans)
