#funtion should do one thing and return something

def say_hello():#defining function
     print('hello')

say_hello() #() -action without that it consider that as variable

#define functions in beginning 
print(say_hello) #print function location

#Default parameters - used when defining the function
def fun_with_param(name='David',emoji='\U0001F606'):
     print(f'hello {name}{emoji}')

#positional arguments -used when invoking/calling the function
fun_with_param('maha','\N{grinning face}') # grinning face 
fun_with_param('bharathi',"\U0001f600") # grinning face 
fun_with_param('devi',"\U0001f600") # grinning face 

#keyword arguments
fun_with_param(emoji='\U0001f600',name='ravi') # bad practice - because making code complicated
fun_with_param(name='ravichandran', emoji='\U0001f600') # this is ok

fun_with_param()


#Return 

def sum(num1,num2):
     return num1+num2

print(sum(4,5))

#nested function -very confusing

def outside_fun(num1,num2):
     def inside_fun(num1,num2):
          return num1+num2
     return inside_fun(num1,num2) #to call inside func

print(outside_fun(1,2)) #inside_fun is not called