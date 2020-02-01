username='supercoder'
password='supersecret'
long_string='''
WOW
O O
---
'''
print(long_string)

first_name='mahabharathi'
last_name='ravichandran'
full_name=first_name+' '+last_name
print(full_name)

#String concatenation
print('hello'+'world')
print('hello','world')

print(type(int((str(100))))) #type conversion

#escape sequence

weather="\n \t it\'s \"kind of \"sunny \n hope u have a good day!"
print(weather)

#Formatted strings
name='mahabharathi'
age=23
print('Hi '+name+' . you are '+str(age)+' year old.') #normal

#Formatted
print(f'Hi {name}. You are {age} years old.')
print('Hi {}. You are {} years old.'.format('mahabharathi','23'))
print('Hi {}. You are {} years old.'.format(name,age))
print('Hi {0}. You are {1} years old.'.format(name,age))
print('Hi {new_name}. You are {new_age} years old.'.format(new_name='maha',new_age=24))

#String indexes
selfish='me me me'
         #01234567
#[start:stop:stepover]
print(selfish[0:8:2])
print(selfish[1:]) #go all the way to end
print(selfish[:]) #start-0 and end - 8
print(selfish[::2]) #start at 0 and end at 8 at stepover
print(selfish[-2]) #go backwards
print(selfish[::-1])#stepover backwards

#immutability
#cannor change character in a strings
#we can reassign
