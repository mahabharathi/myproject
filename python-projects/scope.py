#Scope - What variable you have access to?

#functional scope

total=100 #global scope

def some_fun():
    tot =100   #local scope

def confusion():
    total=110 #local variable -new variable
    return total

print(total)  
print(confusion()) #does not affect the global var
print(total)

#1- start with local
#2 - parent local?
#3 - global
#4 -built in function

def parent():
    total=110 #local variable -new variable
    def child():
        total=120
        return total
    print(total)
    return child()

print(parent()) # if there is no local var it takes the global var


#Global keyword

#parameters are local variable
#To refer the global var inside function 

#not good way , hence pass the total as argument to count
total=0

def count():
    global total #to access the global variable
    total+=1
    return total

print(count())
print(count())
print(count())

total=0

def count1(total):
    total+=1
    return total

print(count1(count1((count1(total)))))

#Non local keyword nonlocal-keyword in python 3
def outer():
    x='local'
    def inner():
        nonlocal x # changes made will affect the global var 
        x='nonlocal'
        print('inner :',x)
    inner()
    print('outer :',x)

outer()

# Why do we need scope?if create all var in global
# avoid computer crash
# memory problem
# cpu utilization 

x ='hello '
print(x[0:5])