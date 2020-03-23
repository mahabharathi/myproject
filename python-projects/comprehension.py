#List comprehensions,set,dict

#normal way
my_list=[]

for char in 'hello':
    my_list.append(char)
    
print(my_list)

#comprehension
my_list1=[param for param in 'hello']

print(my_list1)

my_list2=[num for num in range(100)]
print(my_list2)

my_list3=[num*2 for num in range(100)]

print(my_list3)

my_list4=[num**2 for num in range(100) if num%2==0]

print(my_list4)

print("       ")

#set comprehensions

my_set={char for char in 'hello'}

print(my_set)

print("       ")

#dictionary comprehension
simple_dic={
    'a': 1,
    'b': 2
}
my_dic={key:value**2 for key,value in simple_dic.items() if value%2==0}

print(my_dic)

my_dic={num:num*2 for num in [1,2,3]}

print(my_dic)

#Excerice

some_list=['a','b','c','b','d','m','n','n']

duplicates=list(set([value for value in some_list if some_list.count(value)>1]))

print(duplicates)