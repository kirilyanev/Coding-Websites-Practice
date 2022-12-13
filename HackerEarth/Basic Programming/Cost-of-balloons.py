tests = int(input())

for test in range(0, tests):
    balloon_cost = input().split(' ')
    number_of_participants = int(input())
    first_problem = 0
    second_problem = 0
    result_one = 0
    result_two = 0
    for participant in range(0, number_of_participants):
        curr_participant = input().split(' ')
        if curr_participant[0] == '1':
            first_problem += 1
        if curr_participant[1] == '1':
            second_problem += 1
    result_one = first_problem * int(balloon_cost[0]) + second_problem * int(balloon_cost[1])
    result_two = first_problem * int(balloon_cost[1]) + second_problem * int(balloon_cost[0])

    if result_one > result_two:
        print(result_two)
    else:
        print(result_one)
