import datetime
import time
from array import array

print(datetime.time(5,45,2))
print(datetime.date.today())

#array takes less memory -performs faster
arr=array('i',[1,2,3])
print(arr[0])

#https://docs.python.org/3/py-modindex.html

'''
1.collection module


'''

#Collections module
from collections import Counter,defaultdict,OrderedDict

li=[1,2,3,4,5,6,7,7,8,8,8]
sentence='bdsfwdjfbwebwejhewjdbewhjw'
#print(Counter(li))
#print(Counter(sentence))

dictionary = defaultdict(lambda:'does not exist',{'a':1,'b':2})
print(dictionary['c'])

d=OrderedDict()
d['a']=1
d['b']=1

d2=OrderedDict()
d2['b']=1
d2['a']=1

print(d2==d)

d={'c':100}
d['a']=1
d['b']=1

d2={'c':100}
d2['b']=1
d2['a']=1

print(d2==d)