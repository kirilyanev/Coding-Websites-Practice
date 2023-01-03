# Minutes hand = 3600 seconds 60*60
# 1 minute = 360/60 = 6 degree
# 1 second = 6/60 = 0.1 degree

# Hour hand = 43200 seconds 60*60*12
# 1 hour = 360/12 = 30 degree
# 1 minute = 30/60 = 0.5 degree
# 1 second = 0.5/60 = 0.008333333333

time = input().split(':')
hours = time[0]
minutes = time[1]
time_in_seconds = int(hours) * 60 * 60 + int(minutes) * 60

i = 0
overlap = 0

while i < time_in_seconds + 1:
    hour_hand = i * 0.008333333333
    minute_hand = (i * 0.1) % 360

    if round(hour_hand, 1) == round(minute_hand, 1):
        overlap += 1
        i += 2
    else:
        i += 1

    if i > 43200:
        time_in_seconds -= 43200
        i = 0

print(overlap)
