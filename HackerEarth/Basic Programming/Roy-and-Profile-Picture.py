min_dimension = int(input())
number_of_photos = int(input())

for photo in range(0, number_of_photos):
    curr_photo = input().split(' ')

    if int(curr_photo[0]) < min_dimension or int(curr_photo[1]) < min_dimension:
        print("UPLOAD ANOTHER")
    elif int(curr_photo[0]) == int(curr_photo[1]):
        print("ACCEPTED")
    else:
        print("CROP IT")
