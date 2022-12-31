tests = int(input())

for test in range(0, tests):
    boxes_and_schools = input().split(' ')
    schools = input().split(' ')

    schools_list = list(map(int, schools))
    schools_list.sort()

    boxes = int(boxes_and_schools[0])
    schools_count = int(boxes_and_schools[1])

    visited_schools = 0

    for school in schools_list:
        boxes -= school
        if boxes < 0:
            break
        visited_schools += 1

    print(visited_schools)
