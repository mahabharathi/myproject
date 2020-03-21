#Tuple are list but we cannot modify them (immutable)
# faster than list
# geo graphic loc - user drop loc (uber)
# only two methods - count,index

my_tuple=(1,2,3,4,5,6,7)
# my_tuple[1]='2' -we cannot do this
print(5 in my_tuple)

x,y,z, * other=(1,2,3,4,5)
print(other)
print(my_tuple.count(5)) #count number of 5's 
print(my_tuple.index(5)) # index of 5
print(len(my_tuple))