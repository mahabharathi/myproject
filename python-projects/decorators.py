# Decorators classmethod and staticmethod (starts with @ sign) -super charge function
# functions - first class citizen (acts like variable)
# wrapping function decorator

#Decorator pattern
def my_decorator1(func):
        def wrap(*args,**kwargs):
               print("$$$$$$$$$$$$$$")
               func(*args,**kwargs)
               print("$$$$$$$$$$$$$$")
        return wrap

def my_decorator(func):
        def wrap():
               print("$$$$$$$$$$$$$$")
               func()
               print("$$$$$$$$$$$$$$")
        return wrap

def decor1(func):
        def wrap():
               print("$$$$$$$$$$$$$$")
               func()
               print("$$$$$$$$$$$$$$")
        return wrap
def decor2(func):
        def wrap():
               print("##############")
               func()
               print("##############")
        return wrap
    
@decor1
@decor2
def sayhello():
         print("Hello")
sayhello()

@my_decorator  #same as my_decorator(hello())()
#def hello(func): #Higher Order Function HOF (pass function is function)
 #   func() #jump to passed function as arguments
    
def hello():
         print('hello')
hello()

@my_decorator
def bye():
         print('bye')
bye()

@my_decorator1
def greeting(hello,emoji=':('):
         print(hello,emoji)
greeting('maha')
    
#def greet2(): #Higher Order Function HOF (return function in function)
  #  def func():
 #       return 5
   # return func
    
#new_func=my_decorator(greet)
#new_func()

'''
Why do we need decorators?
    

'''
from time import time

def performance(func):
    def wrap(*args,**kwargs):
        t1=time()
        result=func(*args,**kwargs)
        t2=time()
        #print(f'it took {t2-t1} s')
        return result
    return wrap

@performance
def long_time():
    for i in range(100000000):
        i*5
#long_time()

# Exercise

user1={
    'name' : 'maha',
    'valid' : False
}

def authentication(func):
    def wrap(*args,**kwargs):
        if args[0]['valid']:
            return func(*args,**kwargs)
        else:
            print('not a valid user')
    return wrap

@authentication
def message_friends(user):
    print('message has been sent')
    
message_friends(user1)