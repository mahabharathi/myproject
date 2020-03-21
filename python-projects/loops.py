for item in 'Zero to mastery': #loop char in string Iterable
    print(item)

print("            ")
#String , List, tuple, set

for item in [1,2,3,4,5]: #List
    print(item)

print("            ")
for item in (1,2,3,4,5): #Tuple
    print(item)

print("            ")
for item in {1,2,3,4,5}: #set
    print(item)

print("            ")
print(item) #Value of item is last iterated value

print("            ")
#nested Loop

for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item,x)

#Iterable -String,List,Set,Dictionary,tuple
#Iterate - one by one check each item in the collection

#Dictionary
users = {
    'name' : 'Maha',
    'age' : 20,
    'can_swin' : False
}
print("            ")
for item in users.items():
    print(item) #print key value pair in tuple

print("            ")
for item in users.values():
    print(item) #print values

print("            ")
for item in users.keys():
    print(item) #print keys

print("            ")
for item in users.items(): 
    key,value=item #Tuple unwrapping
    print(key,value) #print key value pair in tuple

print("            ")
for key,value in users.items(): 
    print(key,value) #print key value pair in tuple

#int is not iterable
# for item in 50