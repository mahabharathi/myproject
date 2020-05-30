#Generator - range() yield pass
#iterable -able to loop through

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
            
        except StopIteration:
            break

special_for([1,2,3])

def generator_function(num):
    for i in range(num):   #range is function look like this
        yield i*2
        
g=generator_function(100)
next(g)
next(g)
print(next(g))

print(next(g))

'''
def make_list(number):
    result=[]
    for i in range(number):
        result.append(i*2)
    return result

my_list=make_list(100)
print(my_list)

#print(list(range(1000000)))

'''
from time import time
def performance(func):
        def wrap(*args,**kwargs):
               t1=time()
               func(*args,**kwargs)
               t2=time()
               print(t2-t1)
        return wrap
    
@performance
def long_time():
    print('1')
    for i in range(1000):
        i*5
        
@performance
def long_time2():
    print('2')
    for i in list(range(100)):
        i*5
        
long_time()
long_time2()
