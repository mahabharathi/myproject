#Exercise

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = '$'
empty = ' '

#iterate over picture
   #if 0 print empty space
def show_tree():
    for image in picture:
        for pixel in image:
            if pixel:
                print(fill,end='') #end used to avoid new line
            else:
                print(empty,end='') #end used to avoid new line
        print('') #Need a new line after every image

show_tree()


    # clean
    # Readability
    # Productability
    # DRY -Don't Repeat Yourself

