#arguments
def super_fun(*args): #parameter
    print(args)
    return sum(args)

print(super_fun(1,2,3,4,5))

#*args -acept any num of arguments

#**kwargs

def super_fun1(*args,**kwargs): #parameter
    total=0
    for num in kwargs.values():
        total+=num
    return sum(args)+total

print(super_fun1(1,2,3,4,5, num1=5,num2=10))

#Rule : params , *args, Default params, **kwargs (order)