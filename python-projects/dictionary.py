#Dictionary -data type and data structure- like hash table
#unordered key value pair
# value can be list,string or any data type
# not sorted
# lot of info
# key value may be any data type (key cannot change -num,bool,string (immutable))
# key should be unique (or the values may override the existing same key value)

dictionary = {
    'a' : 1,
    'b' : 2,
    'c' : [1,2,3,4,5],
    'd' : 'hello',
    'e' : True,
    'x' : 3,
    123 : 'hi',
    True : False,
    (1,2) : 'maha'
}

print(dictionary['b'])
#print(dictionary['c'])
print(dictionary[(1,2)])
print(dictionary)


myList = [
    {
    'a' : 1,
    'b' : 2,
    'c' : [1,2,3,4,5],
    'd' : 'hello',
    'e' : True,
    'x' : 3
    },
    {
    'a' : 3,
    'b' : 4,
    'c' : [6,7,8,9],
    'd' : 'hello world',
    'e' : False,
    'x' : 5
    }
]

print(myList[1]['d'])
print(dictionary['c'][3])

user = {
    'basket' : [1,2,3],
    'greet'  : 'hello',
    'age'    : 20
}

print(user.get('age',55))

user2 = dict(name='john')

print(user2)

#Dictionary methods

print('basket' in user)
print('size' in user)
print('age' in user.keys())
print('hello' in user.values())
print(user.popitem())
print(user.items())
print(user.clear())
print(user)
user = user2.copy()
print(user2)

print(user.pop('name'))
print(user)
print(user.update({'age' : 55}))
print(user)