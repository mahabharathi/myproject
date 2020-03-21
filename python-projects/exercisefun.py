def highest_even(li):
    highest_no=0
    for num in li:
        highest_no = num if num%2==0 and highest_no< num else highest_no
    return highest_no


print(highest_even([10,8,3,4,5,2,3]))