#unordered collection of unique object
my_set={1,2,3,4,5,5} #only values
print(my_set) # print unique values
my_set.add(100) #add new value to set
my_set.add(2)
print(my_set)

my_list=[1,2,3,4,5,6,2,5]
print(set(my_list)) #remove dup value from list

# print(my_set[0]) -do not allow indexing
print(len(my_set)) #length
print(list(my_set)) #set to list

new_set=my_set.copy() #copy 
my_set.clear() #clear
print(my_set)
print(new_set)

my_set={1,2,3,4,5,6}
your_set={4,5,6,7,8,9,10}

print(my_set.difference(your_set)) #differences between myset to yourset sets (avoid same values between two sets)
print(my_set.discard(5)) #removes values from set
print(my_set)

print(my_set.difference_update(your_set)) #update differences of myset to yourset
print(my_set)

my_set={1,2,3,4,5,6}
print( my_set & your_set)
print(my_set.intersection(your_set)) #common in two sets my_set & your_set

my_set={4,5}
print(your_set.issuperset(my_set)) #your_set has all values of my_set

print(my_set.isdisjoint(your_set)) #anything in common
print(my_set | your_set) #same as union function

print(my_set.union(your_set)) #join two sets without duplicate
print(my_set.issubset(your_set)) #myset has values of yourset only
