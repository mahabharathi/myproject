#my answers
def highest_even(li):
    highest_no=0
    for num in li:
        highest_no = num if num%2==0 and highest_no< num else highest_no
    return highest_no


print(highest_even([2,10,8,3,4,5,2,3,14]))

#instructor answer
def highest_even_ins(li):
    evens=[]
    for item in li:
        if item % 2 ==0:
            evens.append(item)
    return max(evens)

print(highest_even_ins([2,10,8,3,4,5,2,3,14]))