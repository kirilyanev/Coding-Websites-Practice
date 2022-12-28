tests = int(input())

for tests in range(0, tests):
    curr_guests = input().split(' ')
    boys = int(curr_guests[0])
    girls = int(curr_guests[1])
    room_seats = int(curr_guests[2])

    boys_rooms = boys // room_seats

    if boys % room_seats != 0:
        boys_rooms += 1

    girls_rooms = girls // room_seats

    if girls % room_seats != 0:
        girls_rooms += 1

    required_rooms = boys_rooms + girls_rooms

    print(required_rooms)