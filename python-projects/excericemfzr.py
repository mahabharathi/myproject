from functools import reduce

my_pets = ['sisi','bibi','titi','carla']

def captilize_list(pet):
    return pet.upper()

print(list(map(captilize_list,my_pets)))

my_strings=['a','b','c','d','e']
my_numbers=[5,4,3,2,1]

print(list(zip(my_strings,sorted(my_numbers))))

scores=[73,20,65,19,76,100,88]

def filter_score(item):
    return item>50

print(list(filter(filter_score,scores)))

def reduce_all(acc,item):
    return acc+item

print(reduce(reduce_all,scores,reduce(reduce_all,my_numbers,0)))

print(reduce(reduce_all,(my_numbers+scores)))
