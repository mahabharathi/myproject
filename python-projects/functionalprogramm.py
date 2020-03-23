#pure functions
# should not produce side effects
from functools import reduce

my_list=[1,2,3]
your_list=[10,20,30,40]
def mul_by2(li):
    return li*2

    '''
    new_list=[]
    for num in li:
        new_list.append(num*2)
    
    return new_list
    
    '''

#print(mul_by2([1,2,3]))

#map,filter,zip,and reduce

print(list(map(mul_by2,my_list))) #my_list is immutable ,map create new list
print(my_list)

def only_odd(item):
    return item % 2!=0

print(list(filter(only_odd,my_list))) #my_list is immutable ,map create new list

print(list(zip(my_list,your_list))) #zip items together in two list in tuple [(1, 10), (2, 20), (3, 30)]

def accumulator(acc,item):
    print(acc,item)
    return acc+item

print(reduce(accumulator,my_list,0))